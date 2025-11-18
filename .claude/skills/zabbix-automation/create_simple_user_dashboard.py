#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Simple User Events Dashboard for DC01 (Fixed Version)
"""

import os
import sys
from pathlib import Path

# Force UTF-8 encoding for stdout
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

# Load .env file manually
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
env_path = os.path.join(project_root, '.env')

if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()


def main():
    zabbix_url = os.getenv('ZABBIX_API_URL')
    username = os.getenv('ZABBIX_USERNAME')
    password = os.getenv('ZABBIX_PASSWORD')

    if not all([zabbix_url, username, password]):
        print("Error: Missing required environment variables")
        sys.exit(1)

    print(f"Connecting to Zabbix: {zabbix_url}")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=zabbix_url, user=username, password=password)
        print(f"[OK] Successfully logged in\n")

        # Get DC01 host
        hosts = api.host.get(filter={"host": "DC01"}, output=['hostid', 'host', 'name'])
        if not hosts:
            print("Error: DC01 not found")
            api.logout()
            sys.exit(1)

        hostid = hosts[0]['hostid']
        print(f"Found host: {hosts[0]['name']} (ID: {hostid})\n")

        # Get user-related items
        all_items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_'],
            sortfield='name'
        )

        # Select specific user event items
        user_created = None
        user_deleted = None
        user_modified = None
        failed_login = None
        account_lockout = None
        password_reset = None

        for item in all_items:
            if 'User Account Created' in item['name'] and '4720' in item['key_']:
                user_created = item['itemid']
            elif 'User Account Deleted' in item['name'] and '4726' in item['key_']:
                user_deleted = item['itemid']
            elif 'User Account Modified' in item['name'] and '4738' in item['key_']:
                user_modified = item['itemid']
            elif 'Failed Login' in item['name'] and '4625' in item['key_']:
                failed_login = item['itemid']
            elif 'Account Lockouts' in item['name'] and '4740' in item['key_']:
                account_lockout = item['itemid']
            elif 'Password Reset' in item['name'] and '4724' in item['key_']:
                password_reset = item['itemid']

        print("Found user event items:")
        print(f"  User Created: {user_created}")
        print(f"  User Modified: {user_modified}")
        print(f"  User Deleted: {user_deleted}")
        print(f"  Failed Login: {failed_login}")
        print(f"  Account Lockout: {account_lockout}")
        print(f"  Password Reset: {password_reset}")
        print()

        # Build simple widgets using plaintext type
        widgets = []

        # Widget 1: User Account Events
        if user_created and user_modified and user_deleted:
            widgets.append({
                "type": "plaintext",
                "name": "User Account Events",
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 6,
                "fields": [
                    {"type": 1, "name": "itemids", "value": f"{user_created}\n{user_modified}\n{user_deleted}"},
                    {"type": 0, "name": "show_lines", "value": 15},
                    {"type": 0, "name": "style", "value": 0}
                ]
            })

        # Widget 2: Authentication Events
        if failed_login and account_lockout:
            widgets.append({
                "type": "plaintext",
                "name": "Authentication & Security",
                "x": 12,
                "y": 0,
                "width": 12,
                "height": 6,
                "fields": [
                    {"type": 1, "name": "itemids", "value": f"{failed_login}\n{account_lockout}\n{password_reset}"},
                    {"type": 0, "name": "show_lines", "value": 15},
                    {"type": 0, "name": "style", "value": 0}
                ]
            })

        # Widget 3: Problems
        widgets.append({
            "type": "problems",
            "name": "Active Problems",
            "x": 0,
            "y": 6,
            "width": 24,
            "height": 4,
            "fields": [
                {"type": 0, "name": "show", "value": 1},
                {"type": 1, "name": "hostids", "value": hostid},
                {"type": 0, "name": "show_tags", "value": 3}
            ]
        })

        # Create dashboard
        dashboard_name = "DC01 - User Events"
        dashboard_data = {
            "name": dashboard_name,
            "display_period": 30,
            "auto_start": 1,
            "pages": [{
                "name": "User Events",
                "widgets": widgets
            }]
        }

        # Delete old dashboard if exists
        existing = api.dashboard.get(filter={"name": dashboard_name}, output=['dashboardid'])
        if existing:
            print(f"Deleting old dashboard (ID: {existing[0]['dashboardid']})...")
            api.dashboard.delete(existing[0]['dashboardid'])

        # Also delete the old "DC01 - User Events Dashboard"
        old_dash = api.dashboard.get(filter={"name": "DC01 - User Events Dashboard"}, output=['dashboardid'])
        if old_dash:
            print(f"Deleting old dashboard (ID: {old_dash[0]['dashboardid']})...")
            api.dashboard.delete(old_dash[0]['dashboardid'])

        # Create new dashboard
        result = api.dashboard.create(dashboard_data)
        dashboard_id = result['dashboardids'][0]

        print(f"\n[✓] Dashboard created successfully!")
        print(f"    Dashboard ID: {dashboard_id}")
        print(f"    Dashboard Name: {dashboard_name}")
        print(f"    Widgets: {len(widgets)}")

        base_url = zabbix_url.replace('/api_jsonrpc.php', '')
        print(f"\nDashboard URL:")
        print(f"  {base_url}/zabbix.php?action=dashboard.view&dashboardid={dashboard_id}")
        print(f"\nOr navigate to: Monitoring → Dashboards → '{dashboard_name}'")

        api.logout()
        print("\n[OK] Done")

    except Exception as e:
        import traceback
        print(f"Error: {str(e)}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
