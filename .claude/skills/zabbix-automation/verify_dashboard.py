#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify and fix dashboard configuration
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

        # Get all dashboards
        print("Fetching all dashboards...")
        dashboards = api.dashboard.get(
            output=['dashboardid', 'name', 'display_period', 'auto_start'],
            selectPages=['name', 'widgets']
        )

        print(f"Found {len(dashboards)} dashboards:\n")

        user_events_dashboard = None
        for dash in dashboards:
            print(f"  [{dash['dashboardid']}] {dash['name']}")
            if 'User Events' in dash['name']:
                user_events_dashboard = dash

        if not user_events_dashboard:
            print("\n[!] User Events Dashboard not found!")
            print("Please run create_user_events_dashboard.py again.")
            api.logout()
            sys.exit(1)

        print(f"\n[✓] Found User Events Dashboard:")
        print(f"    ID: {user_events_dashboard['dashboardid']}")
        print(f"    Name: {user_events_dashboard['name']}")
        print(f"    Display Period: {user_events_dashboard['display_period']}s")
        print(f"    Auto Start: {user_events_dashboard['auto_start']}")

        # Check pages
        if 'pages' in user_events_dashboard and user_events_dashboard['pages']:
            page = user_events_dashboard['pages'][0]
            print(f"    Page Name: {page.get('name', 'N/A')}")

            if 'widgets' in page:
                print(f"    Widgets: {len(page['widgets'])}")

                # Show widget details
                print("\n    Widget Details:")
                for idx, widget in enumerate(page['widgets'], 1):
                    print(f"      {idx}. {widget.get('name', 'Unnamed')} ({widget.get('type', 'unknown')})")
            else:
                print("    [!] No widgets found in page!")
        else:
            print("    [!] No pages found in dashboard!")

        # Get the correct URL
        base_url = zabbix_url.replace('/api_jsonrpc.php', '')
        dashboard_url = f"{base_url}/zabbix.php?action=dashboard.view&dashboardid={user_events_dashboard['dashboardid']}"

        print(f"\n{'=' * 80}")
        print(f"\nDashboard URL:")
        print(f"  {dashboard_url}")
        print(f"\nAlternative URL format:")
        print(f"  {base_url}/zabbix.php?action=dashboard.list")
        print(f"  (Then select 'DC01 - User Events Dashboard' from the list)")

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
