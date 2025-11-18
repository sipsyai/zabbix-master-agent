#!/usr/bin/env python3
"""
Setup all ADLogon plugin items on DC01 host
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

ZABBIX_API_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USERNAME = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

class ZabbixAPI:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.auth_token = None
        self.request_id = 1

    def call(self, method, params=None):
        """Make Zabbix API call"""
        headers = {'Content-Type': 'application/json'}

        payload = {
            'jsonrpc': '2.0',
            'method': method,
            'id': self.request_id
        }

        # Add params if provided
        if params is not None:
            payload['params'] = params
        else:
            payload['params'] = {}

        # Add auth token at top level (Zabbix 6.x+)
        if self.auth_token and method != 'user.login':
            payload['auth'] = self.auth_token

        self.request_id += 1

        response = requests.post(self.url, json=payload, headers=headers)
        response.raise_for_status()

        result = response.json()

        if 'error' in result:
            raise Exception(f"Zabbix API error: {result['error']}")

        return result.get('result')

    def login(self):
        """Login to Zabbix"""
        print(f"Logging in to Zabbix at {self.url}...")
        result = self.call('user.login', {
            'username': self.username,
            'password': self.password
        })
        self.auth_token = result
        print("[OK] Successfully authenticated")
        return result

    def logout(self):
        """Logout from Zabbix"""
        if self.auth_token:
            try:
                self.call('user.logout', {})
            except:
                pass  # Ignore logout errors
            self.auth_token = None

    def get_host(self, hostname):
        """Get host by name"""
        result = self.call('host.get', {
            'filter': {'host': hostname},
            'output': ['hostid', 'host', 'name']
        })
        return result[0] if result else None

    def create_item(self, hostid, item_data):
        """Create an item"""
        item_data['hostid'] = hostid
        return self.call('item.create', item_data)

    def get_items(self, hostid, search=None):
        """Get items for a host"""
        params = {
            'hostids': hostid,
            'output': ['itemid', 'name', 'key_'],
        }
        if search:
            params['search'] = {'name': search}
        return self.call('item.get', params)

    def create_trigger(self, trigger_data):
        """Create a trigger"""
        return self.call('trigger.create', trigger_data)


def create_adlogon_items(zapi, hostid, hostname):
    """Create all ADLogon plugin items"""

    # Item definitions
    items_config = [
        {
            'name': 'AD: Logon Failures (Last Hour) - Raw',
            'key': 'ad.logon[failure,1]',
            'type': 'Text',
            'interval': '5m',
            'description': 'Failed logon attempts in the last hour - full JSON data'
        },
        {
            'name': 'AD: Logon Failures (Last Hour) - Count',
            'key': 'ad.logon[failure,1]',
            'type': 'Numeric',
            'interval': '5m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of failed logon attempts in the last hour'
        },
        {
            'name': 'AD: Logon Failures (Last 24 Hours) - Count',
            'key': 'ad.logon[failure,24]',
            'type': 'Numeric',
            'interval': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of failed logon attempts in the last 24 hours'
        },
        {
            'name': 'AD: DC Logon Activity (Last 12 Hours) - Raw',
            'key': 'ad.logon[dc_activity,12]',
            'type': 'Text',
            'interval': '10m',
            'description': 'Domain Controller logon activity - full JSON data'
        },
        {
            'name': 'AD: DC Logon Activity (Last 12 Hours) - Count',
            'key': 'ad.logon[dc_activity,12]',
            'type': 'Numeric',
            'interval': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of DC logon events in the last 12 hours'
        },
        {
            'name': 'AD: Server Logon Activity (Last 24 Hours) - Count',
            'key': 'ad.logon[server_activity,24]',
            'type': 'Numeric',
            'interval': '15m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of member server logon events in the last 24 hours'
        },
        {
            'name': 'AD: Workstation Logon Activity (Last 12 Hours) - Count',
            'key': 'ad.logon[workstation_activity,12]',
            'type': 'Numeric',
            'interval': '15m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of workstation logon events in the last 12 hours'
        },
        {
            'name': 'AD: User Logon Activity (Last 24 Hours) - Raw',
            'key': 'ad.logon[user_activity,24]',
            'type': 'Text',
            'interval': '10m',
            'description': 'User logon activity - full JSON data with unique users'
        },
        {
            'name': 'AD: User Logon Activity (Last 24 Hours) - Count',
            'key': 'ad.logon[user_activity,24]',
            'type': 'Numeric',
            'interval': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Total number of user logon events in the last 24 hours'
        },
        {
            'name': 'AD: User Logon Activity - Unique Users',
            'key': 'ad.logon[user_activity,24]',
            'type': 'Numeric',
            'interval': '10m',
            'preprocessing': [{'type': 12, 'params': '$.unique_users', 'error_handler': 0}],
            'description': 'Number of unique users who logged in during the last 24 hours'
        },
        {
            'name': 'AD: Recent Users (Last Hour)',
            'key': 'ad.logon[recent_users,1]',
            'type': 'Text',
            'interval': '5m',
            'description': 'Recently logged in users - full JSON data'
        },
        {
            'name': 'AD: Last Logon on Workstations',
            'key': 'ad.logon[last_logon,48]',
            'type': 'Text',
            'interval': '30m',
            'description': 'Last logon timestamp per workstation - full JSON data'
        },
        {
            'name': 'AD: Users on Multiple Computers',
            'key': 'ad.logon[multiple_computers,24]',
            'type': 'Text',
            'interval': '15m',
            'description': 'Users logged into multiple computers - full JSON data'
        },
        {
            'name': 'AD: Users on Multiple Computers - Count',
            'key': 'ad.logon[multiple_computers,24]',
            'type': 'Numeric',
            'interval': '15m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of sessions where users are on multiple computers'
        },
        {
            'name': 'AD: RADIUS Logons (Last 6 Hours) - Raw',
            'key': 'ad.logon[radius,6]',
            'type': 'Text',
            'interval': '10m',
            'description': 'RADIUS/NPS authentication events - full JSON data'
        },
        {
            'name': 'AD: RADIUS Logons (Last 6 Hours) - Count',
            'key': 'ad.logon[radius,6]',
            'type': 'Numeric',
            'interval': '10m',
            'preprocessing': [{'type': 12, 'params': '$.count', 'error_handler': 0}],
            'description': 'Number of RADIUS authentication events in the last 6 hours'
        },
    ]

    print(f"\nCreating {len(items_config)} items on host {hostname}...")
    created_count = 0

    for item_config in items_config:
        # Map type to Zabbix value type
        value_type_map = {
            'Numeric': 3,  # Numeric unsigned
            'Text': 4,     # Text
        }

        item_data = {
            'name': item_config['name'],
            'key_': item_config['key'],
            'type': 7,  # Zabbix agent (active)
            'value_type': value_type_map[item_config['type']],
            'delay': item_config['interval'],
            'description': item_config.get('description', ''),
            'history': '7d',
            'trends': '0' if item_config['type'] == 'Text' else '365d',
        }

        # Add preprocessing if defined
        if 'preprocessing' in item_config:
            item_data['preprocessing'] = item_config['preprocessing']

        try:
            result = zapi.create_item(hostid, item_data)
            print(f"  [OK] Created: {item_config['name']}")
            created_count += 1
        except Exception as e:
            if 'already exists' in str(e).lower():
                print(f"  - Exists: {item_config['name']}")
            else:
                print(f"  [FAIL] Failed: {item_config['name']} - {e}")

    print(f"\n[OK] Successfully created {created_count} new items")
    return created_count


def create_triggers(zapi, hostid, hostname):
    """Create triggers for ADLogon items"""

    triggers_config = [
        {
            'description': 'High number of failed logons in the last hour on {HOST.NAME}',
            'expression': f'last(/{hostname}/ad.logon[failure,1])>10',
            'priority': 2,  # Warning
            'comments': 'More than 10 failed logon attempts detected in the last hour. This could indicate a brute force attack or credential issues.'
        },
        {
            'description': 'Very high number of failed logons in the last hour on {HOST.NAME}',
            'expression': f'last(/{hostname}/ad.logon[failure,1])>50',
            'priority': 4,  # High
            'comments': 'More than 50 failed logon attempts detected. Immediate investigation required - possible security incident.'
        },
        {
            'description': 'Users logged into multiple computers on {HOST.NAME}',
            'expression': f'last(/{hostname}/ad.logon[multiple_computers,24])>0',
            'priority': 1,  # Information
            'comments': 'One or more users are logged into multiple computers simultaneously.'
        },
        {
            'description': 'High number of failed logons in 24 hours on {HOST.NAME}',
            'expression': f'last(/{hostname}/ad.logon[failure,24])>100',
            'priority': 3,  # Average
            'comments': 'More than 100 failed logon attempts in the last 24 hours.'
        },
    ]

    print(f"\nCreating {len(triggers_config)} triggers...")
    created_count = 0

    for trigger_config in triggers_config:
        try:
            result = zapi.create_trigger(trigger_config)
            print(f"  [OK] Created: {trigger_config['description']}")
            created_count += 1
        except Exception as e:
            if 'already exists' in str(e).lower():
                print(f"  - Exists: {trigger_config['description']}")
            else:
                print(f"  [FAIL] Failed: {trigger_config['description']} - {e}")

    print(f"\n[OK] Successfully created {created_count} new triggers")
    return created_count


def main():
    print("=" * 70)
    print("ADLogon Plugin - Zabbix Items Setup")
    print("=" * 70)

    # Initialize API
    zapi = ZabbixAPI(ZABBIX_API_URL, ZABBIX_USERNAME, ZABBIX_PASSWORD)

    try:
        # Login
        zapi.login()

        # Get DC01 host
        print("\nSearching for host 'dc01'...")
        host = zapi.get_host('dc01')

        if not host:
            print("[FAIL] Host 'dc01' not found!")
            print("\nAvailable hosts:")
            all_hosts = zapi.call('host.get', {'output': ['host', 'name']})
            for h in all_hosts[:10]:
                print(f"  - {h['host']} ({h['name']})")
            sys.exit(1)

        print(f"[OK] Found host: {host['host']} (ID: {host['hostid']})")

        # Create items
        items_created = create_adlogon_items(zapi, host['hostid'], host['host'])

        # Create triggers
        triggers_created = create_triggers(zapi, host['hostid'], host['host'])

        # Summary
        print("\n" + "=" * 70)
        print("SETUP COMPLETE")
        print("=" * 70)
        print(f"Host: {host['host']}")
        print(f"Items created: {items_created}")
        print(f"Triggers created: {triggers_created}")
        print("\nNext steps:")
        print("1. Go to Monitoring → Latest data")
        print("2. Select host: dc01")
        print("3. Filter by 'AD:' to see all items")
        print("4. Wait a few minutes for data collection")
        print("=" * 70)

    except Exception as e:
        print(f"\n[FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        zapi.logout()


if __name__ == '__main__':
    main()
