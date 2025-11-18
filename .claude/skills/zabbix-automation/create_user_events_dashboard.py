#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Active Directory User Events Dashboard for DC01
"""

import os
import sys
import json
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

# Parse .env file
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
else:
    print(f"Warning: .env file not found at {env_path}")


def main():
    # Get configuration from environment
    zabbix_url = os.getenv('ZABBIX_API_URL')
    username = os.getenv('ZABBIX_USERNAME')
    password = os.getenv('ZABBIX_PASSWORD')

    if not all([zabbix_url, username, password]):
        print("Error: Missing required environment variables")
        sys.exit(1)

    print(f"Connecting to Zabbix: {zabbix_url}")
    print("=" * 80)

    try:
        # Connect to Zabbix API
        api = ZabbixAPI(url=zabbix_url, user=username, password=password)
        print(f"[OK] Successfully logged in as {username}\n")

        # Get DC01 host
        hosts = api.host.get(
            filter={"host": "DC01"},
            output=['hostid', 'host', 'name']
        )

        if not hosts:
            print("Error: Host 'DC01' not found")
            api.logout()
            sys.exit(1)

        host = hosts[0]
        hostid = host['hostid']
        print(f"Found host: {host['name']} (ID: {hostid})\n")

        # Get all items
        print("Fetching user event items...")
        all_items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_', 'value_type'],
            sortfield='name'
        )

        # Categorize user-related events
        user_account_events = []      # Creation, Modification, Deletion
        user_auth_events = []          # Login, Logout
        user_security_events = []      # Lockouts, Password resets
        user_privilege_events = []     # Privilege changes
        user_group_events = []         # Group membership changes
        user_management_summary = []   # Summary counters

        for item in all_items:
            name = item['name']
            key = item['key_']

            # User Account Lifecycle
            if any(x in name for x in ['User Account Created', 'User Account Deleted', 'User Account Modified']):
                user_account_events.append(item)

            # Authentication Events
            elif any(x in name for x in ['Failed Login', 'Oturum Açma', 'logon_activity']):
                user_auth_events.append(item)

            # Security Events
            elif any(x in name for x in ['Account Lockouts', 'Password Reset', 'Auto Account Lockout']):
                user_security_events.append(item)

            # Privilege Events
            elif 'Special Privileges' in name:
                user_privilege_events.append(item)

            # Group Events
            elif any(x in name for x in ['Domain Admins Group', 'Security Group', 'Local Security Group', 'Universal Security Group']):
                user_group_events.append(item)

            # User Management Summary
            elif 'Kullanıcı Yönetimi' in name or 'user_management' in key:
                user_management_summary.append(item)

        print(f"Found user event items:")
        print(f"  - Account Lifecycle: {len(user_account_events)}")
        print(f"  - Authentication: {len(user_auth_events)}")
        print(f"  - Security: {len(user_security_events)}")
        print(f"  - Privileges: {len(user_privilege_events)}")
        print(f"  - Group Changes: {len(user_group_events)}")
        print(f"  - Management Summary: {len(user_management_summary)}")
        print()

        # Create dashboard
        print("Creating User Events Dashboard...")

        dashboard_name = "DC01 - User Events Dashboard"

        # Build widgets
        widgets = []
        widget_y = 0

        # Row 1: User Account Lifecycle + User Management Summary
        if user_account_events:
            widgets.append({
                "type": "plaintext",
                "name": "User Account Lifecycle",
                "x": 0,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in user_account_events])},
                    {"type": 0, "name": "show_lines", "value": 10},
                    {"type": 0, "name": "style", "value": 0}
                ]
            })

        if user_management_summary:
            widgets.append({
                "type": "item",
                "name": "User Management Activity",
                "x": 12,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in user_management_summary])},
                    {"type": 0, "name": "show", "value": 2}
                ]
            })

        widget_y += 5

        # Row 2: Authentication Events + Security Events
        if user_auth_events:
            widgets.append({
                "type": "item",
                "name": "Authentication & Login Events",
                "x": 0,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in user_auth_events])},
                    {"type": 0, "name": "show", "value": 2},
                    {"type": 0, "name": "show_lines", "value": 5}
                ]
            })

        if user_security_events:
            widgets.append({
                "type": "item",
                "name": "User Security Events",
                "x": 12,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in user_security_events])},
                    {"type": 0, "name": "show", "value": 2}
                ]
            })

        widget_y += 5

        # Row 3: Group Changes + Privilege Changes
        if user_group_events:
            widgets.append({
                "type": "item",
                "name": "Group Membership Changes",
                "x": 0,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in user_group_events])},
                    {"type": 0, "name": "show", "value": 2},
                    {"type": 0, "name": "show_lines", "value": 6}
                ]
            })

        if user_privilege_events:
            widgets.append({
                "type": "item",
                "name": "Privilege Assignment Events",
                "x": 12,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in user_privilege_events])},
                    {"type": 0, "name": "show", "value": 2}
                ]
            })

        widget_y += 5

        # Row 4: Problems widget (full width)
        widgets.append({
            "type": "problems",
            "name": "User-Related Problems",
            "x": 0,
            "y": widget_y,
            "width": 24,
            "height": 4,
            "fields": [
                {"type": 0, "name": "show", "value": 1},
                {"type": 1, "name": "hostids", "value": hostid},
                {"type": 1, "name": "severities", "value": "0\n1\n2\n3\n4\n5"},
                {"type": 1, "name": "tags", "value": "User\nAccount\nLogin\nAuthentication"}
            ]
        })

        # Create the dashboard
        dashboard_data = {
            "name": dashboard_name,
            "display_period": 30,
            "auto_start": 1,
            "pages": [
                {
                    "name": "User Events",
                    "widgets": widgets
                }
            ]
        }

        # Check if dashboard already exists
        existing = api.dashboard.get(
            filter={"name": dashboard_name},
            output=['dashboardid', 'name']
        )

        if existing:
            print(f"Dashboard '{dashboard_name}' already exists (ID: {existing[0]['dashboardid']})")
            print("Deleting old dashboard...")
            api.dashboard.delete(existing[0]['dashboardid'])
            print("[OK] Old dashboard deleted")

        # Create new dashboard
        result = api.dashboard.create(dashboard_data)

        dashboard_id = result['dashboardids'][0]
        print(f"\n[✓] User Events Dashboard created successfully!")
        print(f"    Dashboard ID: {dashboard_id}")
        print(f"    Dashboard Name: {dashboard_name}")
        print(f"    Total Widgets: {len(widgets)}")
        print()
        print(f"Dashboard Categories:")
        print(f"  ✓ User Account Lifecycle ({len(user_account_events)} events)")
        print(f"    - User Created (Event 4720)")
        print(f"    - User Modified (Event 4738)")
        print(f"    - User Deleted (Event 4726)")
        print()
        print(f"  ✓ Authentication & Login ({len(user_auth_events)} events)")
        print(f"    - Failed Login Attempts (Event 4625)")
        print(f"    - Logon Activity")
        print()
        print(f"  ✓ User Security ({len(user_security_events)} events)")
        print(f"    - Account Lockouts (Event 4740)")
        print(f"    - Password Resets (Event 4724)")
        print(f"    - Auto Account Lockout (Event 644)")
        print()
        print(f"  ✓ Group Changes ({len(user_group_events)} events)")
        print(f"    - Domain Admins Modified")
        print(f"    - Security Group Changes")
        print(f"    - Universal Group Changes")
        print()
        print(f"  ✓ Privilege Changes ({len(user_privilege_events)} events)")
        print(f"    - Special Privileges Assigned (Event 4672)")
        print()
        print(f"  ✓ User Management Summary ({len(user_management_summary)} counters)")
        print(f"  ✓ Active Problems Widget")

        # Logout
        api.logout()
        print("\n[OK] Logged out successfully")

    except Exception as e:
        import traceback
        print(f"Error: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
