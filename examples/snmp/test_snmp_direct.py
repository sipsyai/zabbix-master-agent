#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Direct SNMP test using pysnmp
"""
import sys

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

try:
    from pysnmp.hlapi.v3arch.asyncio import *
    import asyncio
    print("[INFO] pysnmp library found (v7.x)")
    USE_ASYNC = True
except ImportError:
    try:
        from pysnmp.hlapi import *
        print("[INFO] pysnmp library found (legacy)")
        USE_ASYNC = False
    except ImportError:
        print("[ERROR] pysnmp not installed. Installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pysnmp<6"])
        from pysnmp.hlapi import *
        USE_ASYNC = False

def test_snmp_device(host, port, community):
    """Test SNMP connectivity"""
    print(f"\nTesting {host}:{port}")
    print("-" * 70)

    try:
        # Query sysDescr (1.3.6.1.2.1.1.1.0)
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=1),  # SNMPv2c
            UdpTransportTarget((host, port), timeout=5, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            print(f"  [ERROR] {errorIndication}")
            return False
        elif errorStatus:
            print(f'  [ERROR] {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or "?"}')
            return False
        else:
            for varBind in varBinds:
                print(f'  [OK] {varBind[0]} = {varBind[1]}')
            return True

    except Exception as e:
        print(f"  [ERROR] Exception: {e}")
        return False

def main():
    """Test all SNMP simulators"""

    print("=" * 70)
    print("Direct SNMP Connectivity Test")
    print("=" * 70)

    devices = [
        ('127.0.0.1', 2001, 'custom/public', 'CORE-SWITCH-01'),
        ('127.0.0.1', 2002, 'custom/public', 'EDGE-ROUTER-01'),
        ('127.0.0.1', 2003, 'custom/public', 'PERIMETER-FW-01'),
    ]

    results = {}
    for host, port, community, name in devices:
        success = test_snmp_device(host, port, community)
        results[name] = success

    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    for name, success in results.items():
        status = "[OK]" if success else "[FAILED]"
        print(f"  {status} {name}")

    print()

    if not all(results.values()):
        print("[INFO] Some devices failed SNMP test.")
        print("[INFO] This might explain why Zabbix can't collect data.")
        print("\n[SUGGESTION] Check:")
        print("  1. SNMP simulator configuration")
        print("  2. SNMP community string (custom/public)")
        print("  3. Docker container logs")
    else:
        print("[OK] All devices respond to SNMP queries!")
        print("[INFO] Zabbix should be able to collect data.")

if __name__ == '__main__':
    main()
