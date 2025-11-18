#!/usr/bin/env python3
"""
Collect information from existing Zabbix server
"""

import os
import sys
from pathlib import Path

# Add venv to path if exists
venv_path = Path(__file__).parent / ".claude" / "skills" / "zabbix-automation" / "venv"
if venv_path.exists():
    if os.name == 'nt':
        site_packages = venv_path / "Lib" / "site-packages"
    else:
        site_packages = venv_path / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    sys.path.insert(0, str(site_packages))

try:
    from zabbix_utils import ZabbixAPI
except ImportError:
    print("ERROR: zabbix_utils not installed. Installing...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "zabbix_utils"], check=True)
    from zabbix_utils import ZabbixAPI

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def collect_info():
    """Collect Zabbix server information"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print(f"\n{'='*60}")
    print(" Zabbix Server Information Collector")
    print(f"{'='*60}\n")

    print(f"Connecting to: {api_url}")

    try:
        # Connect to Zabbix API - pass credentials during init to avoid auto-login
        api = ZabbixAPI(url=api_url, user=username, password=password)

        print("OK Connected successfully\n")

        # Get Zabbix version
        version = api.apiinfo.version()
        print(f"Zabbix Version: {version}")
        print(f"-" * 60)

        # Get hosts
        hosts = api.host.get(output=['hostid', 'host', 'status'])
        enabled_hosts = [h for h in hosts if h['status'] == '0']
        disabled_hosts = [h for h in hosts if h['status'] == '1']

        print(f"\n[HOSTS]")
        print(f"  Total Hosts: {len(hosts)}")
        print(f"  - Enabled: {len(enabled_hosts)}")
        print(f"  - Disabled: {len(disabled_hosts)}")

        # Get templates
        templates = api.template.get(output=['templateid', 'name'])
        print(f"\n[TEMPLATES]")
        print(f"  Total Templates: {len(templates)}")

        # Get items
        items = api.item.get(output=['itemid', 'name', 'status'])
        enabled_items = [i for i in items if i['status'] == '0']

        print(f"\n[ITEMS]")
        print(f"  Total Items: {len(items)}")
        print(f"  - Enabled: {len(enabled_items)}")
        print(f"  - Disabled: {len(items) - len(enabled_items)}")

        # Get triggers
        triggers = api.trigger.get(output=['triggerid', 'description', 'status', 'priority'])
        enabled_triggers = [t for t in triggers if t['status'] == '0']

        print(f"\n[TRIGGERS]")
        print(f"  Total Triggers: {len(triggers)}")
        print(f"  - Enabled: {len(enabled_triggers)}")

        # Trigger by severity
        severity_map = {
            '0': 'Not classified',
            '1': 'Information',
            '2': 'Warning',
            '3': 'Average',
            '4': 'High',
            '5': 'Disaster'
        }

        for sev_id, sev_name in severity_map.items():
            count = len([t for t in enabled_triggers if t['priority'] == sev_id])
            if count > 0:
                print(f"    - {sev_name}: {count}")

        # Get users
        users = api.user.get(output=['userid', 'username', 'name', 'surname'])
        print(f"\n[USERS]")
        print(f"  Total Users: {len(users)}")

        # Get host groups
        hostgroups = api.hostgroup.get(output=['groupid', 'name'])
        print(f"\n[HOST GROUPS]")
        print(f"  Total Groups: {len(hostgroups)}")

        # Get actions
        actions = api.action.get(output=['actionid', 'name', 'status'])
        enabled_actions = [a for a in actions if a['status'] == '0']

        print(f"\n[ACTIONS - Notifications]")
        print(f"  Total Actions: {len(actions)}")
        print(f"  - Enabled: {len(enabled_actions)}")

        # Get proxies if any
        proxies = api.proxy.get(output=['proxyid', 'name', 'status'])
        if proxies:
            print(f"\n[PROXIES]")
            print(f"  Total Proxies: {len(proxies)}")
            for proxy in proxies:
                status = "Active" if proxy['status'] == '5' else "Passive"
                print(f"    - {proxy['name']} ({status})")

        # Summary
        print(f"\n{'='*60}")
        print(" SUMMARY")
        print(f"{'='*60}")
        print(f"  Zabbix Version: {version}")
        print(f"  Monitored Hosts: {len(enabled_hosts)}")
        print(f"  Active Items: {len(enabled_items)}")
        print(f"  Active Triggers: {len(enabled_triggers)}")
        print(f"  Templates: {len(templates)}")
        print(f"  Users: {len(users)}")
        print(f"  Proxies: {len(proxies)}")
        print(f"{'='*60}\n")

        # Logout
        api.logout()
        print("OK Disconnected successfully\n")

        return {
            'version': version,
            'hosts': len(hosts),
            'enabled_hosts': len(enabled_hosts),
            'templates': len(templates),
            'items': len(items),
            'enabled_items': len(enabled_items),
            'triggers': len(triggers),
            'enabled_triggers': len(enabled_triggers),
            'users': len(users),
            'proxies': len(proxies)
        }

    except Exception as e:
        print(f"\nERROR: {str(e)}\n")
        return None


if __name__ == "__main__":
    try:
        info = collect_info()
        if info:
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nCancelled by user\n")
        sys.exit(0)
