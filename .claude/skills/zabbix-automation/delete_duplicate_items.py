#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Delete duplicate service.state items that are unsupported
"""

import os
import sys
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
    """Delete duplicate items"""
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
            output=['hostid', 'host', 'name']
        )

        if not hosts:
            print("[-] DC01 host not found!")
            api.logout()
            return

        hostid = hosts[0]['hostid']
        print(f"[+] DC01 Host ID: {hostid}")

        # Get unsupported service.state items
        print("\n[+] Getting duplicate service.state items...")
        items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_', 'type', 'state'],
            search={'key_': 'service.state'},
            filter={'state': '1'}  # Only unsupported
        )

        print(f"[+] Found {len(items)} duplicate service.state items")
        print("=" * 100)

        deleted_items = []

        for item in items:
            print(f"\n[*] Deleting: {item['name']}")
            print(f"    Key: {item['key_']}")
            print(f"    Item ID: {item['itemid']}")

            try:
                api.item.delete(item['itemid'])
                print(f"    [OK] Deleted")
                deleted_items.append(item['name'])
            except Exception as e:
                print(f"    [FAIL] Error: {e}")

        # Summary
        print("\n" + "=" * 100)
        print("[+] DELETION SUMMARY")
        print(f"    Total deleted: {len(deleted_items)}")

        if deleted_items:
            print("\n[+] Deleted items:")
            for name in deleted_items:
                print(f"    ✓ {name}")

        api.logout()
        print("\n[+] Done!")

    except Exception as e:
        print(f"[-] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
