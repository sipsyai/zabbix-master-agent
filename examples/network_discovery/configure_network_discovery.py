#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configure Network Neighbor Discovery (CDP & LLDP) in Zabbix
This script configures Low-Level Discovery rules for discovering network neighbors
using CDP and LLDP protocols via SNMP.
"""
import os
import sys
import json
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

# CDP OIDs (Cisco Discovery Protocol)
CDP_OIDS = {
    'device_id': '1.3.6.1.4.1.9.9.23.1.2.1.1.4',      # cdpCacheDeviceId
    'device_port': '1.3.6.1.4.1.9.9.23.1.2.1.1.5',    # cdpCacheDevicePort
    'platform': '1.3.6.1.4.1.9.9.23.1.2.1.1.6',       # cdpCachePlatform
    'ip_address': '1.3.6.1.4.1.9.9.23.1.2.1.1.8',     # cdpCacheAddress
    'cache_entry': '1.3.6.1.4.1.9.9.23.1.2.1.1.6',    # For discovery
}

# LLDP OIDs (Link Layer Discovery Protocol)
LLDP_OIDS = {
    'remote_system_name': '1.0.8802.1.1.2.1.4.1.1.7', # lldpRemSysName
    'remote_port_id': '1.0.8802.1.1.2.1.4.1.1.9',     # lldpRemPortId
    'chassis_id': '1.0.8802.1.1.2.1.4.1.1.4',         # lldpRemChassisId
    'remote_port_desc': '1.0.8802.1.1.2.1.4.1.1.8',   # lldpRemPortDesc
}

def create_cdp_discovery_rule(api, host_id, host_name, snmp_interface_id):
    """Create CDP Low-Level Discovery rule"""
    print(f"\n[INFO] Creating CDP Discovery Rule for {host_name}...")

    # Discovery rule parameters
    discovery_rule = {
        'name': 'CDP Neighbor Discovery',
        'key_': 'cdp.neighbor.discovery',
        'hostid': host_id,
        'type': 20,  # SNMP agent
        'interfaceid': snmp_interface_id,
        'snmp_oid': 'discovery[{#CDP.IFINDEX},1.3.6.1.4.1.9.9.23.1.2.1.1.6,{#CDP.DEVICEID},1.3.6.1.4.1.9.9.23.1.2.1.1.4]',
        'delay': '1h',
        'status': 0,  # Enabled
        'description': 'Discovers network neighbors using Cisco Discovery Protocol (CDP)',
        'lifetime': '7d',
    }

    try:
        # Check if discovery rule already exists
        existing_rules = api.discoveryrule.get(
            hostids=host_id,
            filter={'key_': discovery_rule['key_']}
        )

        if existing_rules:
            print(f"  [INFO] CDP Discovery Rule already exists (ID: {existing_rules[0]['itemid']})")
            return existing_rules[0]['itemid']

        # Create discovery rule
        result = api.discoveryrule.create(discovery_rule)
        rule_id = result['itemids'][0]
        print(f"  [OK] Created CDP Discovery Rule (ID: {rule_id})")

        # Create item prototypes
        create_cdp_item_prototypes(api, rule_id, host_id, snmp_interface_id)

        return rule_id

    except Exception as e:
        print(f"  [ERROR] Failed to create CDP Discovery Rule: {e}")
        return None

def create_cdp_item_prototypes(api, discovery_rule_id, host_id, interface_id):
    """Create item prototypes for CDP neighbors"""
    print(f"  [INFO] Creating CDP Item Prototypes...")

    item_prototypes = [
        {
            'name': 'CDP Neighbor [{#CDP.DEVICEID}] Device ID',
            'key_': f'cdp.neighbor[{{#CDP.IFINDEX}},deviceid]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{CDP_OIDS["device_id"]}.{{#CDP.IFINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'Device ID of CDP neighbor',
        },
        {
            'name': 'CDP Neighbor [{#CDP.DEVICEID}] Platform',
            'key_': f'cdp.neighbor[{{#CDP.IFINDEX}},platform]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{CDP_OIDS["platform"]}.{{#CDP.IFINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'Platform information of CDP neighbor',
        },
        {
            'name': 'CDP Neighbor [{#CDP.DEVICEID}] Remote Port',
            'key_': f'cdp.neighbor[{{#CDP.IFINDEX}},port]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{CDP_OIDS["device_port"]}.{{#CDP.IFINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'Remote port of CDP neighbor',
        },
        {
            'name': 'CDP Neighbor [{#CDP.DEVICEID}] IP Address',
            'key_': f'cdp.neighbor[{{#CDP.IFINDEX}},ip]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{CDP_OIDS["ip_address"]}.{{#CDP.IFINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'IP address of CDP neighbor',
        },
    ]

    created_count = 0
    for prototype in item_prototypes:
        try:
            prototype['ruleid'] = discovery_rule_id

            # Check if item prototype already exists
            existing_items = api.itemprototype.get(
                discoveryids=discovery_rule_id,
                filter={'key_': prototype['key_']}
            )

            if not existing_items:
                api.itemprototype.create(prototype)
                created_count += 1
        except Exception as e:
            print(f"    [WARN] Failed to create item prototype '{prototype['name']}': {e}")

    print(f"  [OK] Created {created_count} CDP Item Prototypes")

def create_lldp_discovery_rule(api, host_id, host_name, snmp_interface_id):
    """Create LLDP Low-Level Discovery rule"""
    print(f"\n[INFO] Creating LLDP Discovery Rule for {host_name}...")

    # Discovery rule parameters
    discovery_rule = {
        'name': 'LLDP Neighbor Discovery',
        'key_': 'lldp.neighbor.discovery',
        'hostid': host_id,
        'type': 20,  # SNMP agent
        'interfaceid': snmp_interface_id,
        'snmp_oid': 'discovery[{#LLDP.IFINDEX},{#LLDP.REMINDEX},1.0.8802.1.1.2.1.4.1.1.7,{#LLDP.SYSNAME},1.0.8802.1.1.2.1.4.1.1.9]',
        'delay': '1h',
        'status': 0,  # Enabled
        'description': 'Discovers network neighbors using Link Layer Discovery Protocol (LLDP)',
        'lifetime': '7d',
    }

    try:
        # Check if discovery rule already exists
        existing_rules = api.discoveryrule.get(
            hostids=host_id,
            filter={'key_': discovery_rule['key_']}
        )

        if existing_rules:
            print(f"  [INFO] LLDP Discovery Rule already exists (ID: {existing_rules[0]['itemid']})")
            return existing_rules[0]['itemid']

        # Create discovery rule
        result = api.discoveryrule.create(discovery_rule)
        rule_id = result['itemids'][0]
        print(f"  [OK] Created LLDP Discovery Rule (ID: {rule_id})")

        # Create item prototypes
        create_lldp_item_prototypes(api, rule_id, host_id, snmp_interface_id)

        return rule_id

    except Exception as e:
        print(f"  [ERROR] Failed to create LLDP Discovery Rule: {e}")
        return None

def create_lldp_item_prototypes(api, discovery_rule_id, host_id, interface_id):
    """Create item prototypes for LLDP neighbors"""
    print(f"  [INFO] Creating LLDP Item Prototypes...")

    item_prototypes = [
        {
            'name': 'LLDP Neighbor [{#LLDP.SYSNAME}] System Name',
            'key_': f'lldp.neighbor[{{#LLDP.IFINDEX}},{{#LLDP.REMINDEX}},sysname]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{LLDP_OIDS["remote_system_name"]}.{{#LLDP.IFINDEX}}.{{#LLDP.REMINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'System name of LLDP neighbor',
        },
        {
            'name': 'LLDP Neighbor [{#LLDP.SYSNAME}] Remote Port ID',
            'key_': f'lldp.neighbor[{{#LLDP.IFINDEX}},{{#LLDP.REMINDEX}},portid]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{LLDP_OIDS["remote_port_id"]}.{{#LLDP.IFINDEX}}.{{#LLDP.REMINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'Remote port ID of LLDP neighbor',
        },
        {
            'name': 'LLDP Neighbor [{#LLDP.SYSNAME}] Chassis ID',
            'key_': f'lldp.neighbor[{{#LLDP.IFINDEX}},{{#LLDP.REMINDEX}},chassisid]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{LLDP_OIDS["chassis_id"]}.{{#LLDP.IFINDEX}}.{{#LLDP.REMINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'Chassis ID of LLDP neighbor',
        },
        {
            'name': 'LLDP Neighbor [{#LLDP.SYSNAME}] Remote Port Description',
            'key_': f'lldp.neighbor[{{#LLDP.IFINDEX}},{{#LLDP.REMINDEX}},portdesc]',
            'hostid': host_id,
            'type': 20,  # SNMP agent
            'interfaceid': interface_id,
            'snmp_oid': f'{LLDP_OIDS["remote_port_desc"]}.{{#LLDP.IFINDEX}}.{{#LLDP.REMINDEX}}',
            'value_type': 4,  # Text
            'delay': '1h',
            'description': 'Remote port description of LLDP neighbor',
        },
    ]

    created_count = 0
    for prototype in item_prototypes:
        try:
            prototype['ruleid'] = discovery_rule_id

            # Check if item prototype already exists
            existing_items = api.itemprototype.get(
                discoveryids=discovery_rule_id,
                filter={'key_': prototype['key_']}
            )

            if not existing_items:
                api.itemprototype.create(prototype)
                created_count += 1
        except Exception as e:
            print(f"    [WARN] Failed to create item prototype '{prototype['name']}': {e}")

    print(f"  [OK] Created {created_count} LLDP Item Prototypes")

def main():
    """Main function"""

    print("=" * 70)
    print("Network Neighbor Discovery Configuration (CDP & LLDP)")
    print("=" * 70)
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
            output=['hostid', 'host', 'name', 'status'],
            selectInterfaces=['interfaceid', 'type', 'ip', 'port']
        )

        if not hosts:
            print("[ERROR] No SNMP devices found!")
            print("[INFO] Please run add_snmp_devices.py first")
            api.logout()
            sys.exit(1)

        print(f"[INFO] Found {len(hosts)} SNMP devices")
        print()

        # Configure discovery rules for each host
        for host in hosts:
            print("=" * 70)
            print(f"Configuring: {host['name']} ({host['host']})")
            print("-" * 70)

            # Check if host has SNMP interface
            snmp_interfaces = [i for i in host['interfaces'] if i['type'] == '2']
            if not snmp_interfaces:
                print(f"  [WARN] No SNMP interface found, skipping...")
                continue

            snmp_interface_id = snmp_interfaces[0]['interfaceid']

            # Create CDP Discovery Rule
            cdp_rule_id = create_cdp_discovery_rule(api, host['hostid'], host['name'], snmp_interface_id)

            # Create LLDP Discovery Rule
            lldp_rule_id = create_lldp_discovery_rule(api, host['hostid'], host['name'], snmp_interface_id)

            if cdp_rule_id or lldp_rule_id:
                print(f"\n  [OK] Network neighbor discovery configured for {host['name']}")
            else:
                print(f"\n  [WARN] Failed to configure discovery for {host['name']}")

        print()
        print("=" * 70)
        print("[OK] Network neighbor discovery configuration completed!")
        print("=" * 70)
        print()
        print("[INFO] Discovery rules will run every 1 hour")
        print("[INFO] You can manually execute them in Zabbix UI:")
        print("        Configuration -> Hosts -> Discovery -> Execute now")
        print()
        print("[INFO] After discovery runs, neighbor information will appear in:")
        print("        Monitoring -> Latest data -> Filter by host")
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
