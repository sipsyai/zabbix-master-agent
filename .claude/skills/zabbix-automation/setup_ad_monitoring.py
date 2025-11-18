#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Active Directory Services Monitoring Setup for DC01
Creates monitoring items and triggers for critical AD services
"""

import os
import sys
from typing import List, Dict
from pathlib import Path

# Windows console encoding fix
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from zabbix_utils import ZabbixAPI

# Kritik AD Servisleri
AD_SERVICES = [
    {
        "name": "NTDS",
        "description": "Active Directory Domain Services",
        "key": "service.info[NTDS,state]",
        "priority": "high"
    },
    {
        "name": "DNS",
        "description": "DNS Server",
        "key": "service.info[DNS,state]",
        "priority": "high"
    },
    {
        "name": "Netlogon",
        "description": "Netlogon",
        "key": "service.info[Netlogon,state]",
        "priority": "high"
    },
    {
        "name": "KDC",
        "description": "Kerberos Key Distribution Center",
        "key": "service.info[KDC,state]",
        "priority": "high"
    },
    {
        "name": "DFSR",
        "description": "DFS Replication",
        "key": "service.info[DFSR,state]",
        "priority": "average"
    },
    {
        "name": "W32Time",
        "description": "Windows Time Service",
        "key": "service.info[W32Time,state]",
        "priority": "average"
    },
    {
        "name": "ADWS",
        "description": "Active Directory Web Services",
        "key": "service.info[ADWS,state]",
        "priority": "average"
    }
]


def load_env_file():
    """Load environment variables from .env file"""
    # Find .env file in project root
    # Navigate from .claude/skills/zabbix-automation to project root
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent.parent.parent
    env_file = project_root / '.env'

    if not env_file.exists():
        print(f"[-] .env file not found at: {env_file}")
        return False

    print(f"[+] Loading credentials from: {env_file}")

    # Read and parse .env file
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

    return True


def connect_to_zabbix():
    """Connect to Zabbix API using credentials from .env file"""
    # Load .env file
    if not load_env_file():
        sys.exit(1)

    url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print(f"[+] Connecting to Zabbix API: {url}")
    print(f"[+] Username: {username}")

    try:
        api = ZabbixAPI(url=url, user=username, password=password)

        version = api.version
        print(f"[+] Connection successful! Zabbix version: {version}")
        return api
    except Exception as e:
        print(f"[-] Connection error: {e}")
        sys.exit(1)


def find_host(api: ZabbixAPI, hostname: str) -> Dict:
    """Find host by hostname and get interface info"""
    print(f"\n[+] Searching for host: {hostname}")

    try:
        hosts = api.host.get(
            filter={"host": hostname},
            output=["hostid", "host", "name", "status"],
            selectInterfaces=["interfaceid", "type", "ip", "main"]
        )

        if not hosts:
            print(f"[-] Host not found: {hostname}")
            sys.exit(1)

        host = hosts[0]
        status = "Enabled" if host['status'] == '0' else "Disabled"
        print(f"[+] Host found!")
        print(f"    - Host ID: {host['hostid']}")
        print(f"    - Hostname: {host['host']}")
        print(f"    - Display Name: {host['name']}")
        print(f"    - Status: {status}")

        # Find Zabbix agent interface (type 1)
        agent_interface = None
        for interface in host.get('interfaces', []):
            if interface['type'] == '1' and interface['main'] == '1':  # Type 1 = Zabbix agent, main = primary
                agent_interface = interface
                break

        if not agent_interface and host.get('interfaces'):
            # If no main interface, take the first agent interface
            for interface in host['interfaces']:
                if interface['type'] == '1':
                    agent_interface = interface
                    break

        if not agent_interface:
            print(f"[-] No Zabbix agent interface found for host {hostname}")
            sys.exit(1)

        host['agent_interfaceid'] = agent_interface['interfaceid']
        print(f"    - Agent Interface ID: {agent_interface['interfaceid']} ({agent_interface.get('ip', 'N/A')})")

        return host
    except Exception as e:
        print(f"[-] Host search error: {e}")
        sys.exit(1)


def get_existing_items(api: ZabbixAPI, hostid: str) -> List[str]:
    """Get existing item keys on the host"""
    try:
        items = api.item.get(
            hostids=hostid,
            output=["itemid", "key_"]
        )
        return [item['key_'] for item in items]
    except Exception as e:
        print(f"[-] Item listing error: {e}")
        return []


def create_service_items(api: ZabbixAPI, hostid: str, interfaceid: str) -> List[Dict]:
    """Create monitoring items for AD services"""
    print(f"\n[+] Creating monitoring items for AD services...")

    existing_keys = get_existing_items(api, hostid)
    created_items = []
    skipped_items = []

    for service in AD_SERVICES:
        key = service['key']

        # Skip if item already exists
        if key in existing_keys:
            print(f"    [!] Item already exists, skipping: {service['name']}")
            skipped_items.append(service['name'])
            continue

        try:
            # Create item for Windows service state
            # type: 0 = Zabbix agent
            # value_type: 3 = numeric (unsigned)
            # delay: 60s = check every minute
            item = api.item.create(
                name=f"Service state: {service['description']}",
                key_=key,
                hostid=hostid,
                interfaceid=interfaceid,
                type=0,  # Zabbix agent
                value_type=3,  # Numeric (unsigned)
                delay="60s",
                history="7d",
                trends="365d",
                description=f"Monitors the state of {service['description']} service.\n0 - running, 1 - paused, 2 - start pending, 3 - pause pending, 4 - continue pending, 5 - stop pending, 6 - stopped, 7 - unknown, 255 - no such service"
            )

            created_items.append({
                'service': service,
                'itemid': item['itemids'][0]
            })

            print(f"    [+] Item created: {service['name']} (ID: {item['itemids'][0]})")

        except Exception as e:
            print(f"    [-] Item creation error ({service['name']}): {e}")

    print(f"\n[+] Summary: {len(created_items)} items created, {len(skipped_items)} items already existed")
    return created_items


def get_priority_value(priority: str) -> int:
    """Convert trigger priority string to Zabbix severity value"""
    priorities = {
        "not_classified": 0,
        "information": 1,
        "warning": 2,
        "average": 3,
        "high": 4,
        "disaster": 5
    }
    return priorities.get(priority, 3)


def create_service_triggers(api: ZabbixAPI, hostname: str, created_items: List[Dict]) -> List[str]:
    """Create triggers for each service"""
    print(f"\n[+] Creating service triggers...")

    created_triggers = []

    for item_info in created_items:
        service = item_info['service']
        key = service['key']

        try:
            # Trigger when service is not running (state != 0)
            # Alert for Stopped (6) or Unknown (7) states
            expression = f"last(/{hostname}/{key})<>0"

            severity = get_priority_value(service['priority'])

            trigger = api.trigger.create(
                description=f"{service['description']} service is not running on {{HOST.NAME}}",
                expression=expression,
                priority=severity,
                comments=f"The {service['description']} service has stopped or is in an abnormal state. This is a critical Active Directory component.",
                manual_close=1  # Allow manual close
            )

            created_triggers.append(service['name'])
            print(f"    [+] Trigger created: {service['name']} (ID: {trigger['triggerids'][0]})")

        except Exception as e:
            print(f"    [-] Trigger creation error ({service['name']}): {e}")

    print(f"\n[+] Total {len(created_triggers)} triggers created")
    return created_triggers


def verify_monitoring(api: ZabbixAPI, hostid: str):
    """Verify monitoring setup"""
    print(f"\n[+] Verifying monitoring setup...")

    try:
        # Check items
        items = api.item.get(
            hostids=hostid,
            output=["itemid", "name", "key_", "status"],
            search={"key_": "service.info"},
            searchByAny=True
        )

        print(f"    [OK] {len(items)} AD service items found")

        # List active items
        print("\n[+] Active monitoring items:")
        for item in items:
            if item['status'] == '0':  # Enabled
                print(f"    - {item['name']} ({item['key_']})")

        # Check triggers
        triggers = api.trigger.get(
            hostids=hostid,
            output=["triggerid", "description", "priority", "status"],
            search={"description": "service"},
            searchByAny=True
        )

        print(f"\n[+] Active triggers:")
        priority_names = {0: "Not classified", 1: "Information", 2: "Warning", 3: "Average", 4: "High", 5: "Disaster"}
        for trigger in triggers:
            if trigger['status'] == '0':  # Enabled
                priority = priority_names.get(int(trigger['priority']), "Unknown")
                print(f"    - [{priority}] {trigger['description']}")

        print(f"\n    [OK] Total: {len(triggers)} AD service triggers configured")

    except Exception as e:
        print(f"[-] Verification error: {e}")


def main():
    """Main function"""
    print("=" * 70)
    print("  Active Directory Services Monitoring Setup")
    print("  DC01 Host - Critical AD Services Monitor")
    print("=" * 70)

    # Connect to Zabbix API
    api = connect_to_zabbix()

    try:
        # Find DC01 host
        host = find_host(api, "DC01")
        hostid = host['hostid']
        hostname = host['host']
        interfaceid = host['agent_interfaceid']

        # Create items for AD services
        created_items = create_service_items(api, hostid, interfaceid)

        # Create triggers for each service
        if created_items:
            create_service_triggers(api, hostname, created_items)
        else:
            print("\n[!] No new items created, skipping trigger creation")
            print("[!] Please check existing items manually for triggers")

        # Verify setup
        verify_monitoring(api, hostid)

        print("\n" + "=" * 70)
        print("[+] Operation completed!")
        print("=" * 70)
        print("\nNext steps:")
        print("1. Check DC01 host 'Latest data' section in Zabbix web interface")
        print("2. Verify that service states are being collected properly")
        print("3. Test by stopping a service to see if trigger activates")
        print("4. Configure notification media type and actions if needed")

    finally:
        # Close API connection
        try:
            api.logout()
            print("\n[+] Zabbix API connection closed")
        except:
            pass


if __name__ == "__main__":
    main()
