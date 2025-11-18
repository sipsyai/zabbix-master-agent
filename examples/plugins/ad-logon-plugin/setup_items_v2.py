#!/usr/bin/env python3
"""
Setup all ADLogon plugin items on DC01 host using pyzabbix
"""

import os
import sys
from dotenv import load_dotenv
from pyzabbix import ZabbixAPI

# Load environment variables
load_dotenv()

ZABBIX_API_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USERNAME = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

def create_adlogon_items(api, hostid):
    """Create all ADLogon plugin items"""

    # Item definitions
    items_config = [
        {
            'name': 'AD: Logon Failures (Last Hour) - Raw',
            'key_': 'ad.logon[failure,1]',
            'type': 7,  # Zabbix agent (active)
            'value_type': 4,  # Text
            'delay': '5m',
            'description': 'Failed logon attempts in the last hour - full JSON data',
            'history': '7d',
            'trends': '0'
        },
        {
            'name': 'AD: Logon Failures (Last Hour) - Count',
            'key_': 'ad.logon[failure,1]',
            'type': 7,
            'value_type': 3,  # Numeric unsigned
            'delay': '5m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of failed logon attempts in the last hour',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: Logon Failures (Last 24 Hours) - Count',
            'key_': 'ad.logon[failure,24]',
            'type': 7,
            'value_type': 3,
            'delay': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of failed logon attempts in the last 24 hours',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: DC Logon Activity (Last 12 Hours) - Raw',
            'key_': 'ad.logon[dc_activity,12]',
            'type': 7,
            'value_type': 4,
            'delay': '10m',
            'description': 'Domain Controller logon activity - full JSON data',
            'history': '7d',
            'trends': '0'
        },
        {
            'name': 'AD: DC Logon Activity (Last 12 Hours) - Count',
            'key_': 'ad.logon[dc_activity,12]',
            'type': 7,
            'value_type': 3,
            'delay': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of DC logon events in the last 12 hours',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: Server Logon Activity (Last 24 Hours) - Count',
            'key_': 'ad.logon[server_activity,24]',
            'type': 7,
            'value_type': 3,
            'delay': '15m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of member server logon events in the last 24 hours',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: Workstation Logon Activity (Last 12 Hours) - Count',
            'key_': 'ad.logon[workstation_activity,12]',
            'type': 7,
            'value_type': 3,
            'delay': '15m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of workstation logon events in the last 12 hours',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: User Logon Activity (Last 24 Hours) - Raw',
            'key_': 'ad.logon[user_activity,24]',
            'type': 7,
            'value_type': 4,
            'delay': '10m',
            'description': 'User logon activity - full JSON data with unique users',
            'history': '7d',
            'trends': '0'
        },
        {
            'name': 'AD: User Logon Activity (Last 24 Hours) - Count',
            'key_': 'ad.logon[user_activity,24]',
            'type': 7,
            'value_type': 3,
            'delay': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Total number of user logon events in the last 24 hours',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: User Logon Activity - Unique Users',
            'key_': 'ad.logon[user_activity,24]',
            'type': 7,
            'value_type': 3,
            'delay': '10m',
            'preprocessing': [{'type': 12, 'params': '$.unique_users', 'error_handler': 0}],
            'description': 'Number of unique users who logged in during the last 24 hours',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: Recent Users (Last Hour)',
            'key_': 'ad.logon[recent_users,1]',
            'type': 7,
            'value_type': 4,
            'delay': '5m',
            'description': 'Recently logged in users - full JSON data',
            'history': '7d',
            'trends': '0'
        },
        {
            'name': 'AD: Last Logon on Workstations',
            'key_': 'ad.logon[last_logon,48]',
            'type': 7,
            'value_type': 4,
            'delay': '30m',
            'description': 'Last logon timestamp per workstation - full JSON data',
            'history': '7d',
            'trends': '0'
        },
        {
            'name': 'AD: Users on Multiple Computers',
            'key_': 'ad.logon[multiple_computers,24]',
            'type': 7,
            'value_type': 4,
            'delay': '15m',
            'description': 'Users logged into multiple computers - full JSON data',
            'history': '7d',
            'trends': '0'
        },
        {
            'name': 'AD: Users on Multiple Computers - Count',
            'key_': 'ad.logon[multiple_computers,24]',
            'type': 7,
            'value_type': 3,
            'delay': '15m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of sessions where users are on multiple computers',
            'history': '7d',
            'trends': '365d'
        },
        {
            'name': 'AD: RADIUS Logons (Last 6 Hours) - Raw',
            'key_': 'ad.logon[radius,6]',
            'type': 7,
            'value_type': 4,
            'delay': '10m',
            'description': 'RADIUS/NPS authentication events - full JSON data',
            'history': '7d',
            'trends': '0'
        },
        {
            'name': 'AD: RADIUS Logons (Last 6 Hours) - Count',
            'key_': 'ad.logon[radius,6]',
            'type': 7,
            'value_type': 3,
            'delay': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of RADIUS authentication events in the last 6 hours',
            'history': '7d',
            'trends': '365d'
        },
    ]

    print(f"\nCreating {len(items_config)} items...")
    created_count = 0

    for item_config in items_config:
        item_config['hostid'] = hostid

        try:
            result = api.item.create(item_config)
            print(f"  [OK] Created: {item_config['name']}")
            created_count += 1
        except Exception as e:
            error_msg = str(e)
            if 'already exists' in error_msg.lower():
                print(f"  - Exists: {item_config['name']}")
            else:
                print(f"  [FAIL] {item_config['name']}: {error_msg}")

    print(f"\n[OK] Successfully created {created_count} new items")
    return created_count


def create_triggers(api, hostid, hostname):
    """Create triggers for ADLogon items"""

    triggers_config = [
        {
            'description': f'High number of failed logons in the last hour on {hostname}',
            'expression': f'last(/{hostname}/ad.logon[failure,1])>10',
            'priority': 2,  # Warning
            'comments': 'More than 10 failed logon attempts detected in the last hour.'
        },
        {
            'description': f'Very high number of failed logons in the last hour on {hostname}',
            'expression': f'last(/{hostname}/ad.logon[failure,1])>50',
            'priority': 4,  # High
            'comments': 'More than 50 failed logon attempts detected - possible security incident.'
        },
        {
            'description': f'Users logged into multiple computers on {hostname}',
            'expression': f'last(/{hostname}/ad.logon[multiple_computers,24])>0',
            'priority': 1,  # Information
            'comments': 'One or more users are logged into multiple computers simultaneously.'
        },
        {
            'description': f'High number of failed logons in 24 hours on {hostname}',
            'expression': f'last(/{hostname}/ad.logon[failure,24])>100',
            'priority': 3,  # Average
            'comments': 'More than 100 failed logon attempts in the last 24 hours.'
        },
    ]

    print(f"\nCreating {len(triggers_config)} triggers...")
    created_count = 0

    for trigger_config in triggers_config:
        try:
            result = api.trigger.create(trigger_config)
            print(f"  [OK] Created: {trigger_config['description']}")
            created_count += 1
        except Exception as e:
            error_msg = str(e)
            if 'already exists' in error_msg.lower():
                print(f"  - Exists: {trigger_config['description']}")
            else:
                print(f"  [FAIL] {trigger_config['description']}: {error_msg}")

    print(f"\n[OK] Successfully created {created_count} new triggers")
    return created_count


def main():
    print("=" * 70)
    print("ADLogon Plugin - Zabbix Items Setup (v2)")
    print("=" * 70)

    # Initialize API
    print(f"\nConnecting to Zabbix at {ZABBIX_API_URL}...")
    api = ZabbixAPI(ZABBIX_API_URL)

    try:
        # Login
        api.login(user=ZABBIX_USERNAME, password=ZABBIX_PASSWORD)
        print("[OK] Successfully authenticated")

        # Get DC01 host
        print("\nSearching for host 'DC01'...")
        hosts = api.host.get(filter={'host': 'DC01'}, output=['hostid', 'host', 'name'])

        if not hosts:
            print("[FAIL] Host 'dc01' not found!")
            print("\nAvailable hosts:")
            all_hosts = api.host.get(output=['host', 'name'], limit=10)
            for h in all_hosts:
                print(f"  - {h['host']} ({h.get('name', 'N/A')})")
            sys.exit(1)

        host = hosts[0]
        print(f"[OK] Found host: {host['host']} (ID: {host['hostid']})")

        # Create items
        items_created = create_adlogon_items(api, host['hostid'])

        # Create triggers
        triggers_created = create_triggers(api, host['hostid'], host['host'])

        # Summary
        print("\n" + "=" * 70)
        print("SETUP COMPLETE")
        print("=" * 70)
        print(f"Host: {host['host']}")
        print(f"Items created: {items_created}")
        print(f"Triggers created: {triggers_created}")
        print("\nNext steps:")
        print("1. Go to Monitoring -> Latest data")
        print("2. Select host: dc01")
        print("3. Filter by 'AD:' to see all items")
        print("4. Wait a few minutes for data collection")
        print("=" * 70)

    except Exception as e:
        print(f"\n[FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
