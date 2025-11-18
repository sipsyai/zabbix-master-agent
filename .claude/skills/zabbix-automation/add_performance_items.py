#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add missing performance metrics to DC01 host
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
        print(f"Found host: {host['name']} (ID: {hostid})")

        # Get host interfaces
        interfaces = api.hostinterface.get(
            hostids=hostid,
            output=['interfaceid', 'type', 'main']
        )

        if not interfaces:
            print("Error: No interfaces found for DC01")
            api.logout()
            sys.exit(1)

        # Get the main agent interface
        agent_interface = None
        for iface in interfaces:
            if iface['type'] == '1' and iface['main'] == '1':  # Type 1 = Zabbix agent
                agent_interface = iface['interfaceid']
                break

        if not agent_interface:
            agent_interface = interfaces[0]['interfaceid']

        print(f"Using interface ID: {agent_interface}\n")

        # Define new items to add
        new_items = [
            # CPU Metrics - Per Core
            {
                "name": "CPU: Core 0 Utilization",
                "key_": 'perf_counter_en["\\Processor Information(0,_Total)\\% Processor Time"]',
                "type": 0,  # Zabbix agent
                "value_type": 0,  # Float
                "delay": "60s",
                "units": "%",
                "description": "CPU utilization for Core 0"
            },
            {
                "name": "CPU: Core 1 Utilization",
                "key_": 'perf_counter_en["\\Processor Information(1,_Total)\\% Processor Time"]',
                "type": 0,
                "value_type": 0,
                "delay": "60s",
                "units": "%",
                "description": "CPU utilization for Core 1"
            },
            {
                "name": "CPU: Interrupts per Second",
                "key_": 'perf_counter_en["\\Processor Information(_total)\\Interrupts/sec"]',
                "type": 0,
                "value_type": 0,
                "delay": "60s",
                "units": "ops",
                "description": "Number of interrupts per second"
            },

            # Memory Metrics
            {
                "name": "Memory: Utilization Percentage",
                "key_": "vm.memory.util",
                "type": 0,
                "value_type": 0,
                "delay": "60s",
                "units": "%",
                "description": "Memory utilization in percentage"
            },
            {
                "name": "Memory: Page File Usage",
                "key_": 'perf_counter_en["\\Paging File(_Total)\\% Usage"]',
                "type": 0,
                "value_type": 0,
                "delay": "60s",
                "units": "%",
                "description": "Page file usage percentage"
            },
            {
                "name": "Memory: Page File Bytes",
                "key_": 'perf_counter_en["\\Paging File(_Total)\\% Usage Peak"]',
                "type": 0,
                "value_type": 0,
                "delay": "300s",
                "units": "%",
                "description": "Peak page file usage"
            },

            # Disk Metrics - Latency
            {
                "name": "Disk: Avg Disk sec/Read",
                "key_": 'perf_counter_en["\\PhysicalDisk(_Total)\\Avg. Disk sec/Read"]',
                "type": 0,
                "value_type": 0,
                "delay": "60s",
                "units": "s",
                "description": "Average time in seconds to read from disk"
            },
            {
                "name": "Disk: Avg Disk sec/Write",
                "key_": 'perf_counter_en["\\PhysicalDisk(_Total)\\Avg. Disk sec/Write"]',
                "type": 0,
                "value_type": 0,
                "delay": "60s",
                "units": "s",
                "description": "Average time in seconds to write to disk"
            },
            # Network Metrics
            {
                "name": "Network: Utilization Percentage",
                "key_": "net.if.util",
                "type": 0,
                "value_type": 0,
                "delay": "60s",
                "units": "%",
                "description": "Network interface utilization percentage"
            },
        ]

        print(f"Adding {len(new_items)} new performance items...\n")

        added_count = 0
        failed_count = 0

        for item in new_items:
            try:
                item['hostid'] = hostid
                item['interfaceid'] = agent_interface

                result = api.item.create(item)
                print(f"[✓] Added: {item['name']}")
                added_count += 1

            except Exception as e:
                print(f"[✗] Failed to add '{item['name']}': {str(e)}")
                failed_count += 1

        print("\n" + "=" * 80)
        print(f"\nSummary:")
        print(f"  Successfully added: {added_count}")
        print(f"  Failed: {failed_count}")
        print(f"  Total attempted: {len(new_items)}")

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
