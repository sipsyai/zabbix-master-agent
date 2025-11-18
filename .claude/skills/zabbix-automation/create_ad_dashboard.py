#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Active Directory Dashboard for DC01
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

        # Get all AD-related items
        print("Fetching AD-related items...")
        all_items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_', 'value_type'],
            sortfield='name'
        )

        # Categorize AD items
        ad_services = []
        ad_replication = []
        ad_events = []
        ad_security = []
        ldap_items = []
        kerberos_items = []
        dns_items = []
        lsass_items = []
        ntds_items = []

        for item in all_items:
            name = item['name']
            key = item['key_']

            if 'Service state:' in name and any(x in name for x in ['NTDS', 'ADWS', 'KDC', 'Netlogon', 'DNS', 'DFSR', 'W32Time', 'Intersite']):
                ad_services.append(item)
            elif 'AD Replication' in name:
                ad_replication.append(item)
            elif 'AD Events:' in name and 'Count' in name:
                ad_events.append(item)
            elif name.startswith('AD:') and 'Event' in name:
                ad_security.append(item)
            elif 'LDAP' in name:
                ldap_items.append(item)
            elif 'Kerberos' in name:
                kerberos_items.append(item)
            elif 'DNS:' in name:
                dns_items.append(item)
            elif 'LSASS' in name:
                lsass_items.append(item)
            elif 'NTDS' in name:
                ntds_items.append(item)

        print(f"Found AD items:")
        print(f"  - Services: {len(ad_services)}")
        print(f"  - Replication: {len(ad_replication)}")
        print(f"  - Events: {len(ad_events)}")
        print(f"  - Security: {len(ad_security)}")
        print(f"  - LDAP: {len(ldap_items)}")
        print(f"  - Kerberos: {len(kerberos_items)}")
        print(f"  - DNS: {len(dns_items)}")
        print(f"  - LSASS: {len(lsass_items)}")
        print(f"  - NTDS: {len(ntds_items)}")
        print()

        # Create dashboard
        print("Creating Active Directory Dashboard...")

        dashboard_name = "DC01 - Active Directory Monitoring"

        # Build widgets
        widgets = []
        widget_y = 0

        # Widget 1: AD Services Status (top row)
        service_items_str = '\n'.join([item['itemid'] for item in ad_services[:8]])
        widgets.append({
            "type": "item",
            "name": "AD Services Status",
            "x": 0,
            "y": widget_y,
            "width": 12,
            "height": 4,
            "fields": [
                {"type": 1, "name": "itemids", "value": service_items_str},  # type 1 = string
                {"type": 0, "name": "show", "value": 2},  # type 0 = integer, value as int
                {"type": 0, "name": "show_lines", "value": 8}
            ]
        })

        # Widget 2: AD Events Summary
        widgets.append({
            "type": "item",
            "name": "AD Events Summary",
            "x": 12,
            "y": widget_y,
            "width": 12,
            "height": 4,
            "fields": [
                {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in ad_events[:8]])},
                {"type": 0, "name": "show", "value": 2}
            ]
        })

        widget_y += 4

        # Widget 3: AD Replication Graph
        if ad_replication:
            replication_items = [item['itemid'] for item in ad_replication]
            widgets.append({
                "type": "graph",
                "name": "AD Replication Metrics",
                "x": 0,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 0, "name": "source_type", "value": 1},  # 1 = items, as integer
                    {"type": 1, "name": "itemid", "value": replication_items[0] if replication_items else ""},
                ]
            })

        # Widget 4: LDAP Metrics Graph
        if ldap_items:
            widgets.append({
                "type": "graph",
                "name": "LDAP Performance",
                "x": 12,
                "y": widget_y,
                "width": 12,
                "height": 5,
                "fields": [
                    {"type": 0, "name": "source_type", "value": 1},
                    {"type": 1, "name": "itemid", "value": ldap_items[0]['itemid']},
                ]
            })

        widget_y += 5

        # Widget 5: DNS Metrics
        if dns_items:
            widgets.append({
                "type": "item",
                "name": "DNS Metrics",
                "x": 0,
                "y": widget_y,
                "width": 8,
                "height": 4,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in dns_items[:5]])},
                    {"type": 0, "name": "show", "value": 2}
                ]
            })

        # Widget 6: LSASS Process
        if lsass_items:
            widgets.append({
                "type": "item",
                "name": "LSASS Process",
                "x": 8,
                "y": widget_y,
                "width": 8,
                "height": 4,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in lsass_items])},
                    {"type": 0, "name": "show", "value": 2}
                ]
            })

        # Widget 7: AD Problems
        widgets.append({
            "type": "problems",
            "name": "Active Directory Problems",
            "x": 16,
            "y": widget_y,
            "width": 8,
            "height": 4,
            "fields": [
                {"type": 0, "name": "show", "value": 1},  # Show problems
                {"type": 1, "name": "hostids", "value": hostid},
                {"type": 1, "name": "severities", "value": "0\n1\n2\n3\n4\n5"}
            ]
        })

        widget_y += 4

        # Widget 8: Security Events (bottom section)
        if ad_security:
            widgets.append({
                "type": "item",
                "name": "AD Security Events",
                "x": 0,
                "y": widget_y,
                "width": 24,
                "height": 5,
                "fields": [
                    {"type": 1, "name": "itemids", "value": '\n'.join([item['itemid'] for item in ad_security[:10]])},
                    {"type": 0, "name": "show", "value": 2},
                    {"type": 0, "name": "show_lines", "value": 10}
                ]
            })

        # Create the dashboard
        dashboard_data = {
            "name": dashboard_name,
            "display_period": 30,
            "auto_start": 1,
            "pages": [
                {
                    "name": "Overview",
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
        print(f"\n[✓] Dashboard created successfully!")
        print(f"    Dashboard ID: {dashboard_id}")
        print(f"    Dashboard Name: {dashboard_name}")
        print(f"    Total Widgets: {len(widgets)}")
        print()
        print(f"Dashboard includes:")
        print(f"  ✓ AD Services Status ({len(ad_services)} services)")
        print(f"  ✓ AD Events Summary ({len(ad_events)} event types)")
        print(f"  ✓ AD Replication Metrics ({len(ad_replication)} metrics)")
        print(f"  ✓ LDAP Performance ({len(ldap_items)} metrics)")
        print(f"  ✓ DNS Metrics ({len(dns_items)} metrics)")
        print(f"  ✓ LSASS Process Monitoring ({len(lsass_items)} metrics)")
        print(f"  ✓ Security Events ({len(ad_security)} event types)")
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
