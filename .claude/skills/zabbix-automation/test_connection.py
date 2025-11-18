#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Zabbix API connection
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

    print(f"[+] Loading credentials from: {env_file}")

    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                os.environ[key] = value
                if 'PASSWORD' not in key:
                    print(f"    {key} = {value}")

    return True


def main():
    """Test connection"""
    if not load_env_file():
        sys.exit(1)

    url = os.getenv('ZABBIX_API_URL')
    username = os.getenv('ZABBIX_USERNAME')
    password = os.getenv('ZABBIX_PASSWORD')

    print(f"\n[+] URL: {url}")
    print(f"[+] Username: {username}")
    print(f"[+] Password length: {len(password) if password else 0}")

    try:
        print("\n[+] Creating ZabbixAPI object and logging in...")
        api = ZabbixAPI(url=url, user=username, password=password)

        print(f"[+] Login successful!")
        print(f"[+] Zabbix version: {api.version}")

        api.logout()
        print("[+] Logged out successfully")

    except Exception as e:
        print(f"[-] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
