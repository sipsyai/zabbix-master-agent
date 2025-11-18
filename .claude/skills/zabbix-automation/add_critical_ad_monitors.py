#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add critical Active Directory monitoring items to DC01
"""

import os
import sys
import json
from pathlib import Path

# Windows console encoding fix
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from zabbix_utils import ZabbixAPI


def load_env_file():
    """Load environment variables from .env file"""
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent.parent.parent
    env_file = project_root / '.env'

    if not env_file.exists():
        print(f"[-] .env file not found at: {env_file}")
        return False

    print(f"[+] Loading credentials from: {env_file}")

    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                os.environ[key] = value

    return True


def main():
    """Add critical AD monitoring items"""
    if not load_env_file():
        sys.exit(1)

    url = os.getenv('ZABBIX_API_URL')
    username = os.getenv('ZABBIX_USERNAME')
    password = os.getenv('ZABBIX_PASSWORD')

    try:
        print("\n[+] Connecting to Zabbix API...")
        api = ZabbixAPI(url=url, user=username, password=password)
        print(f"[+] Connected! Zabbix version: {api.version}")

        # Get DC01 host
        print("\n[+] Getting DC01 host...")
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output=['hostid', 'host', 'name'],
            selectInterfaces=['interfaceid', 'type']
        )

        if not hosts:
            print("[-] DC01 host not found!")
            api.logout()
            return

        hostid = hosts[0]['hostid']

        # Get agent interface ID (type 1)
        agent_interface = None
        for iface in hosts[0]['interfaces']:
            if iface['type'] == '1':  # Zabbix agent
                agent_interface = iface['interfaceid']
                break

        if not agent_interface:
            print("[-] No Zabbix agent interface found!")
            api.logout()
            return

        print(f"[+] DC01 Host ID: {hostid}")
        print(f"[+] Agent Interface ID: {agent_interface}")

        # Define critical monitoring items
        critical_items = [
            # 1. AD REPLICATION - ÇOK KRİTİK
            {
                'name': 'AD Replication: Pending Synchronizations',
                'key_': r'perf_counter_en["\NTDS\DRA Pending Replication Synchronizations"]',
                'type': 0,  # Zabbix agent
                'value_type': 3,  # Numeric unsigned
                'delay': '60s',
                'description': 'Number of directory synchronizations that are queued but not yet processed',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'AD Replication: Inbound Objects/sec',
                'key_': r'perf_counter_en["\NTDS\DRA Inbound Objects/sec"]',
                'type': 0,
                'value_type': 0,  # Numeric float
                'delay': '60s',
                'description': 'Rate at which objects are received from replication partners',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'AD Replication: Outbound Objects/sec',
                'key_': r'perf_counter_en["\NTDS\DRA Outbound Objects/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate at which objects are sent to replication partners',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'AD Replication: Sync Requests Made',
                'key_': r'perf_counter_en["\NTDS\DRA Sync Requests Made"]',
                'type': 0,
                'value_type': 3,
                'delay': '60s',
                'description': 'Number of sync requests made to replication partners',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'AD Replication: Highest USN',
                'key_': r'perf_counter_en["\NTDS\DRA Highest USN Issued (High part)"]',
                'type': 0,
                'value_type': 3,
                'delay': '300s',
                'description': 'Highest Update Sequence Number issued',
                'history': '7d',
                'trends': '365d'
            },

            # 2. NTDS DATABASE PERFORMANCE
            {
                'name': 'NTDS Database: Cache Hit Ratio',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache % Hit"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Percentage of database file page requests served from cache',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'NTDS Database: Cache Size (MB)',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache Size (MB)"]',
                'type': 0,
                'value_type': 3,
                'delay': '300s',
                'description': 'Amount of system memory used for database cache',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'NTDS Database: I/O Reads/sec',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Database Reads/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of database read operations',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'NTDS Database: I/O Writes/sec',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Database Writes/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of database write operations',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'NTDS Database: Log Writes/sec',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Log Writes/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of transaction log write operations',
                'history': '7d',
                'trends': '365d'
            },

            # 3. LDAP PERFORMANCE
            {
                'name': 'LDAP: Client Sessions',
                'key_': r'perf_counter_en["\NTDS\LDAP Client Sessions"]',
                'type': 0,
                'value_type': 3,
                'delay': '60s',
                'description': 'Number of connected LDAP client sessions',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'LDAP: Successful Binds/sec',
                'key_': r'perf_counter_en["\NTDS\LDAP Successful Binds/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of successful LDAP binds',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'LDAP: Searches/sec',
                'key_': r'perf_counter_en["\NTDS\LDAP Searches/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of LDAP search operations',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'LDAP: Writes/sec',
                'key_': r'perf_counter_en["\NTDS\LDAP Writes/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of LDAP write operations',
                'history': '7d',
                'trends': '365d'
            },

            # 4. LSASS PROCESS MONITORING
            {
                'name': 'LSASS: CPU Usage',
                'key_': 'proc.cpu.util[lsass.exe]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'LSASS process CPU utilization',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'LSASS: Memory Usage',
                'key_': 'proc.mem[lsass.exe,,,,rss]',
                'type': 0,
                'value_type': 3,
                'delay': '60s',
                'description': 'LSASS process memory usage in bytes',
                'history': '7d',
                'trends': '365d'
            },

            # 5. DNS SERVER STATISTICS
            {
                'name': 'DNS: Total Query Received/sec',
                'key_': r'perf_counter_en["\DNS\Total Query Received/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of DNS queries received',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'DNS: Dynamic Update Received/sec',
                'key_': r'perf_counter_en["\DNS\Dynamic Update Received/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of dynamic DNS updates received',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'DNS: Secure Update Received/sec',
                'key_': r'perf_counter_en["\DNS\Secure Update Received/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of secure DNS updates received',
                'history': '7d',
                'trends': '365d'
            },

            # 6. SYSVOL HEALTH
            {
                'name': 'SYSVOL: Policy Count',
                'key_': r'vfs.dir.count["C:\Windows\SYSVOL\domain\Policies"]',
                'type': 0,
                'value_type': 3,
                'delay': '300s',
                'description': 'Number of Group Policy objects in SYSVOL',
                'history': '7d',
                'trends': '365d'
            },

            # 7. KERBEROS KDC PERFORMANCE
            {
                'name': 'Kerberos: AS Requests/sec',
                'key_': r'perf_counter_en["\Kerberos Key Distribution Center\AS Requests/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of Authentication Service requests',
                'history': '7d',
                'trends': '365d'
            },
            {
                'name': 'Kerberos: TGS Requests/sec',
                'key_': r'perf_counter_en["\Kerberos Key Distribution Center\TGS Requests/sec"]',
                'type': 0,
                'value_type': 0,
                'delay': '60s',
                'description': 'Rate of Ticket Granting Service requests',
                'history': '7d',
                'trends': '365d'
            }
        ]

        print(f"\n[+] Adding {len(critical_items)} critical monitoring items...")
        print("=" * 80)

        added_items = []
        skipped_items = []
        failed_items = []

        for item in critical_items:
            try:
                print(f"\n[*] Adding: {item['name']}")
                print(f"    Key: {item['key_']}")

                # Check if item already exists
                existing = api.item.get(
                    hostids=hostid,
                    filter={'key_': item['key_']},
                    output=['itemid']
                )

                if existing:
                    print(f"    [SKIP] Item already exists (ID: {existing[0]['itemid']})")
                    skipped_items.append(item['name'])
                    continue

                # Create the item
                result = api.item.create(
                    hostid=hostid,
                    name=item['name'],
                    key_=item['key_'],
                    type=item['type'],
                    value_type=item['value_type'],
                    delay=item['delay'],
                    interfaceid=agent_interface,
                    description=item.get('description', ''),
                    history=item.get('history', '7d'),
                    trends=item.get('trends', '365d')
                )

                print(f"    [OK] Item created (ID: {result['itemids'][0]})")
                added_items.append(item['name'])

            except Exception as e:
                print(f"    [FAIL] Error: {e}")
                failed_items.append({'name': item['name'], 'error': str(e)})

        # Summary
        print("\n" + "=" * 80)
        print("\n[+] SUMMARY")
        print(f"    Added: {len(added_items)}")
        print(f"    Skipped: {len(skipped_items)}")
        print(f"    Failed: {len(failed_items)}")

        if added_items:
            print("\n[+] Successfully added items:")
            for name in added_items:
                print(f"    ✓ {name}")

        if skipped_items:
            print("\n[+] Skipped items (already exist):")
            for name in skipped_items:
                print(f"    - {name}")

        if failed_items:
            print("\n[-] Failed items:")
            for item in failed_items:
                print(f"    ✗ {item['name']}")
                print(f"      Error: {item['error']}")

        # Now add critical triggers
        print("\n" + "=" * 80)
        print("[+] Adding critical triggers...")

        triggers = [
            {
                'description': 'AD Replication: High pending synchronizations on DC01',
                'expression': r'last(/DC01/perf_counter_en["\NTDS\DRA Pending Replication Synchronizations"])>5',
                'priority': 4,  # High
                'comments': 'More than 5 replication synchronizations are pending'
            },
            {
                'description': 'NTDS Database: Low cache hit ratio on DC01',
                'expression': r'avg(/DC01/perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache % Hit"],5m)<90',
                'priority': 3,  # Average
                'comments': 'Database cache hit ratio below 90% for 5 minutes'
            },
            {
                'description': 'LSASS: High CPU usage on DC01',
                'expression': r'avg(/DC01/proc.cpu.util[lsass.exe],5m)>80',
                'priority': 3,  # Average
                'comments': 'LSASS process CPU usage above 80% for 5 minutes'
            },
            {
                'description': 'SYSVOL: Policy folder empty on DC01',
                'expression': r'last(/DC01/vfs.dir.count["C:\Windows\SYSVOL\domain\Policies"])=0',
                'priority': 5,  # Disaster
                'comments': 'SYSVOL Policies folder is empty - critical issue'
            }
        ]

        added_triggers = []
        failed_triggers = []

        for trigger in triggers:
            try:
                print(f"\n[*] Adding trigger: {trigger['description']}")

                result = api.trigger.create(
                    description=trigger['description'],
                    expression=trigger['expression'],
                    priority=trigger['priority'],
                    comments=trigger.get('comments', '')
                )

                print(f"    [OK] Trigger created (ID: {result['triggerids'][0]})")
                added_triggers.append(trigger['description'])

            except Exception as e:
                print(f"    [FAIL] Error: {e}")
                failed_triggers.append({'name': trigger['description'], 'error': str(e)})

        print("\n" + "=" * 80)
        print("\n[+] TRIGGER SUMMARY")
        print(f"    Added: {len(added_triggers)}")
        print(f"    Failed: {len(failed_triggers)}")

        if added_triggers:
            print("\n[+] Successfully added triggers:")
            for name in added_triggers:
                print(f"    ✓ {name}")

        if failed_triggers:
            print("\n[-] Failed triggers:")
            for trigger in failed_triggers:
                print(f"    ✗ {trigger['name']}")
                print(f"      Error: {trigger['error']}")

        api.logout()
        print("\n[+] Done!")

    except Exception as e:
        print(f"[-] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
