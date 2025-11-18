#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
View Network Neighbors discovered via CDP and LLDP
Displays network topology information collected from SNMP devices
"""
import os
import sys
import json
from datetime import datetime
from dotenv import load_dotenv
from zabbix_utils import ZabbixAPI

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Load environment variables
load_dotenv()

# Zabbix connection details
ZABBIX_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USER = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

def format_timestamp(timestamp):
    """Convert Unix timestamp to readable format"""
    try:
        return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return 'N/A'

def get_neighbor_items(api, host_id, protocol='cdp'):
    """Get neighbor items for a specific protocol (cdp or lldp)"""
    items = api.item.get(
        hostids=host_id,
        search={'key_': f'{protocol}.neighbor'},
        searchByAny=True,
        output=['itemid', 'name', 'key_', 'lastvalue', 'lastclock', 'state'],
        sortfield='name',
        sortorder='ASC'
    )
    return items

def parse_neighbor_info(items, protocol='cdp'):
    """Parse neighbor items into structured data"""
    neighbors = {}

    for item in items:
        # Extract neighbor identifier from item name
        # CDP: "CDP Neighbor [DEVICE-NAME] Device ID"
        # LLDP: "LLDP Neighbor [DEVICE-NAME] System Name"

        try:
            name_parts = item['name'].split('[')
            if len(name_parts) < 2:
                continue

            neighbor_id = name_parts[1].split(']')[0]
            field_name = name_parts[1].split(']')[1].strip()

            if neighbor_id not in neighbors:
                neighbors[neighbor_id] = {
                    'id': neighbor_id,
                    'last_seen': item.get('lastclock', '0'),
                    'protocol': protocol.upper()
                }

            # Map field names
            field_mapping = {
                'Device ID': 'device_id',
                'Platform': 'platform',
                'Remote Port': 'remote_port',
                'IP Address': 'ip_address',
                'System Name': 'system_name',
                'Remote Port ID': 'port_id',
                'Chassis ID': 'chassis_id',
                'Remote Port Description': 'port_description'
            }

            for field_key, field_value in field_mapping.items():
                if field_key in field_name:
                    neighbors[neighbor_id][field_value] = item.get('lastvalue', 'N/A')
                    break

        except Exception as e:
            continue

    return list(neighbors.values())

def display_neighbors(host_name, cdp_neighbors, lldp_neighbors):
    """Display neighbor information in a formatted way"""

    print("=" * 90)
    print(f"Network Neighbors for: {host_name}")
    print("=" * 90)

    # Display CDP Neighbors
    if cdp_neighbors:
        print("\n[CDP - Cisco Discovery Protocol Neighbors]")
        print("-" * 90)
        for neighbor in cdp_neighbors:
            print(f"\n  Device: {neighbor.get('device_id', neighbor.get('id', 'Unknown'))}")
            print(f"    Platform:     {neighbor.get('platform', 'N/A')}")
            print(f"    Remote Port:  {neighbor.get('remote_port', 'N/A')}")
            print(f"    IP Address:   {neighbor.get('ip_address', 'N/A')}")
            print(f"    Last Seen:    {format_timestamp(neighbor.get('last_seen', '0'))}")
    else:
        print("\n[CDP - Cisco Discovery Protocol]")
        print("-" * 90)
        print("  No CDP neighbors discovered yet")
        print("  (Run discovery rule or wait for next scheduled discovery)")

    # Display LLDP Neighbors
    if lldp_neighbors:
        print("\n\n[LLDP - Link Layer Discovery Protocol Neighbors]")
        print("-" * 90)
        for neighbor in lldp_neighbors:
            print(f"\n  System: {neighbor.get('system_name', neighbor.get('id', 'Unknown'))}")
            print(f"    Port ID:          {neighbor.get('port_id', 'N/A')}")
            print(f"    Port Description: {neighbor.get('port_description', 'N/A')}")
            print(f"    Chassis ID:       {neighbor.get('chassis_id', 'N/A')}")
            print(f"    Last Seen:        {format_timestamp(neighbor.get('last_seen', '0'))}")
    else:
        print("\n\n[LLDP - Link Layer Discovery Protocol]")
        print("-" * 90)
        print("  No LLDP neighbors discovered yet")
        print("  (Run discovery rule or wait for next scheduled discovery)")

    print("\n" + "=" * 90)

def create_topology_map(hosts_neighbors):
    """Create a simple ASCII topology map"""
    print("\n" + "=" * 90)
    print("Network Topology Map")
    print("=" * 90)
    print()

    for host_name, data in hosts_neighbors.items():
        cdp_neighbors = data['cdp']
        lldp_neighbors = data['lldp']

        if cdp_neighbors or lldp_neighbors:
            print(f"┌─ {host_name}")

            # CDP connections
            for neighbor in cdp_neighbors:
                device_id = neighbor.get('device_id', neighbor.get('id', 'Unknown'))
                remote_port = neighbor.get('remote_port', 'N/A')
                print(f"│  ├─[CDP]─> {device_id} (Port: {remote_port})")

            # LLDP connections
            for neighbor in lldp_neighbors:
                system_name = neighbor.get('system_name', neighbor.get('id', 'Unknown'))
                port_id = neighbor.get('port_id', 'N/A')
                print(f"│  ├─[LLDP]─> {system_name} (Port: {port_id})")

            print("│")

    print("=" * 90)

def main():
    """Main function"""

    print("=" * 90)
    print("Network Neighbor Viewer (CDP & LLDP)")
    print("=" * 90)
    print()

    # Connect to Zabbix API
    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Connected to Zabbix API")
        print(f"[OK] Zabbix version: {api.version}")
        print()
    except Exception as e:
        print(f"[ERROR] Failed to connect: {e}")
        sys.exit(1)

    # Get SNMP devices
    device_names = ['CORE-SWITCH-01', 'EDGE-ROUTER-01', 'PERIMETER-FW-01']

    try:
        # Get hosts
        hosts = api.host.get(
            filter={'host': device_names},
            output=['hostid', 'host', 'name', 'status']
        )

        if not hosts:
            print("[ERROR] No SNMP devices found!")
            api.logout()
            sys.exit(1)

        print(f"[INFO] Found {len(hosts)} SNMP devices")
        print()

        hosts_neighbors = {}

        # Get neighbor information for each host
        for host in hosts:
            print(f"[INFO] Retrieving neighbors for {host['name']}...")

            # Get CDP neighbors
            cdp_items = get_neighbor_items(api, host['hostid'], 'cdp')
            cdp_neighbors = parse_neighbor_info(cdp_items, 'cdp')

            # Get LLDP neighbors
            lldp_items = get_neighbor_items(api, host['hostid'], 'lldp')
            lldp_neighbors = parse_neighbor_info(lldp_items, 'lldp')

            # Store for topology map
            hosts_neighbors[host['name']] = {
                'cdp': cdp_neighbors,
                'lldp': lldp_neighbors
            }

            # Display neighbors
            display_neighbors(host['name'], cdp_neighbors, lldp_neighbors)
            print()

        # Create topology map
        create_topology_map(hosts_neighbors)

        print()
        print("[INFO] Neighbor information updated in real-time from Zabbix")
        print("[INFO] To manually trigger discovery:")
        print("        Zabbix UI -> Configuration -> Hosts -> Discovery -> Execute now")
        print()

        api.logout()

    except Exception as e:
        print(f"[ERROR] Operation failed: {e}")
        import traceback
        traceback.print_exc()
        api.logout()
        sys.exit(1)

if __name__ == '__main__':
    main()
