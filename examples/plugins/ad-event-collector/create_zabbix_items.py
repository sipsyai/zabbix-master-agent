#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Zabbix trapper items for AD Event Collector
"""

import os
import sys
import json
import io
from dotenv import load_dotenv
from zabbix_utils import ZabbixAPI

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load environment variables
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
env_path = os.path.join(root_dir, '.env')
load_dotenv(env_path)

ZABBIX_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USER = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

def load_event_mapping():
    """Load event mapping configuration"""
    config_path = os.path.join(os.path.dirname(__file__), 'event-mapping.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_items(api, hostid, config):
    """Create trapper items for each event category"""

    items_config = []

    # Create item for each category
    for category_key, category in config['categories'].items():
        # Main category item (raw JSON)
        items_config.append({
            'name': f"AD Events: {category['name']} - Raw",
            'key_': f"ad.events[{category_key}]",
            'type': 2,  # Zabbix trapper
            'value_type': 4,  # Text
            'delay': 0,  # No passive checks
            'description': category['description'],
            'history': '30d',  # 30 days retention
            'trends': '0'
        })

        # Event count item (dependent item with preprocessing)
        items_config.append({
            'name': f"AD Events: {category['name']} - Count",
            'key_': f"ad.events[{category_key},count]",
            'type': 2,  # Zabbix trapper
            'value_type': 3,  # Numeric unsigned
            'delay': 0,
            'description': f"Number of {category['name']} events",
            'history': '90d',  # 90 days for metrics
            'trends': '365d'
        })

    # Summary item
    items_config.append({
        'name': 'AD Events: Overall Summary',
        'key_': 'ad.events[summary]',
        'type': 2,  # Zabbix trapper
        'value_type': 4,  # Text
        'delay': 0,
        'description': 'Overall summary of all AD events collection',
        'history': '30d',
        'trends': '0'
    })

    # Total events count
    items_config.append({
        'name': 'AD Events: Total Count',
        'key_': 'ad.events[total_count]',
        'type': 2,
        'value_type': 3,
        'delay': 0,
        'description': 'Total number of AD events collected',
        'history': '90d',
        'trends': '365d'
    })

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

    return created_count

def create_triggers(api, hostid, hostname, config):
    """Create triggers for AD events"""

    triggers_config = [
        {
            'description': f'High number of failed logons on {hostname}',
            'expression': f'last(/{hostname}/ad.events[logon_activity,count])>50',
            'priority': 3,  # Average
            'comments': 'More than 50 failed logon attempts detected.'
        },
        {
            'description': f'Critical AD changes detected on {hostname}',
            'expression': f'last(/{hostname}/ad.events[security_permissions,count])>0',
            'priority': 4,  # High
            'comments': 'Security or permission changes in Active Directory.'
        },
        {
            'description': f'Privileged group membership changed on {hostname}',
            'expression': f'last(/{hostname}/ad.events[critical_groups,count])>0',
            'priority': 4,  # High
            'comments': 'Changes to Domain Admins, Enterprise Admins or other critical groups.'
        },
        {
            'description': f'User account changes detected on {hostname}',
            'expression': f'last(/{hostname}/ad.events[user_management,count])>10',
            'priority': 2,  # Warning
            'comments': 'More than 10 user account changes in the collection period.'
        },
        {
            'description': f'GPO or Schema changes on {hostname}',
            'expression': f'last(/{hostname}/ad.events[gpo_management,count])>0 or last(/{hostname}/ad.events[schema_changes,count])>0',
            'priority': 3,  # Average
            'comments': 'Group Policy or AD Schema modifications detected.'
        }
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

    return created_count

def main():
    print("=" * 80)
    print("AD Event Collector - Zabbix Items Setup")
    print("=" * 80)

    # Load event mapping
    print("\nLoading event mapping configuration...")
    config = load_event_mapping()
    print(f"[OK] Loaded {len(config['categories'])} event categories")

    # Connect to Zabbix
    print(f"\nConnecting to Zabbix at {ZABBIX_URL}...")

    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Authenticated successfully")

        # Get DC01 host
        print("\nSearching for DC01 host...")
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output=['hostid', 'host', 'name']
        )

        if not hosts:
            print("[FAIL] DC01 host not found!")
            sys.exit(1)

        host = hosts[0]
        print(f"[OK] Found host: {host['host']} (ID: {host['hostid']})")

        # Create items
        items_created = create_items(api, host['hostid'], config)

        # Create triggers
        triggers_created = create_triggers(api, host['hostid'], host['host'], config)

        # Summary
        print("\n" + "=" * 80)
        print("SETUP COMPLETE")
        print("=" * 80)
        print(f"Host: {host['host']}")
        print(f"Items created: {items_created}")
        print(f"Triggers created: {triggers_created}")
        print("\nNext steps:")
        print("1. Run PowerShell collector script on DC01")
        print("2. Wait for first data collection")
        print("3. Check Zabbix UI for incoming data")
        print("4. Setup Grafana dashboards")
        print("=" * 80)

    except Exception as e:
        print(f"\n[FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        api.logout()

if __name__ == '__main__':
    main()
