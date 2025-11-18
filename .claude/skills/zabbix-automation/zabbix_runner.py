#!/usr/bin/env python3
"""
Zabbix Automation Runner Script

Provides interactive interface for Zabbix operations:
- API operations (user, host, item, template management)
- Sender operations (sending metrics to Zabbix server/proxy)
- Getter operations (retrieving values from Zabbix agents)
"""

import os
import sys
import subprocess
import json
from pathlib import Path


class Colors:
    """ANSI color codes"""
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def check_python_version():
    """Verify Python version"""
    if sys.version_info < (3, 8):
        print(f"{Colors.FAIL}ERROR: Python 3.8+ required{Colors.ENDC}")
        sys.exit(1)


def setup_virtualenv():
    """Create venv if needed, return python executable path"""
    venv_path = Path(__file__).parent / "venv"
    
    if venv_path.exists():
        print(f"{Colors.OKGREEN}Virtual environment found{Colors.ENDC}")
    else:
        print("Creating virtual environment...")
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(venv_path)],
                check=True,
                capture_output=True
            )
            print(f"{Colors.OKGREEN}Venv created successfully{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}Failed to create venv: {e}{Colors.ENDC}")
            sys.exit(1)
    
    if os.name == 'nt':
        return venv_path / "Scripts" / "python.exe"
    else:
        return venv_path / "bin" / "python"


def install_dependencies(python_exe):
    """Install dependencies from requirements.txt"""
    req_file = Path(__file__).parent / "requirements.txt"
    
    if not req_file.exists():
        print(f"{Colors.WARNING}requirements.txt not found{Colors.ENDC}")
        return
    
    print("Installing dependencies...")
    try:
        subprocess.run(
            [str(python_exe), "-m", "pip", "install", "-q", "-r", str(req_file)],
            check=True,
            capture_output=True
        )
        print(f"{Colors.OKGREEN}Dependencies installed{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Failed to install: {e}{Colors.ENDC}")
        sys.exit(1)


def get_env_or_prompt(env_var, prompt_text, default=None, password=False):
    """Get value from env or prompt"""
    value = os.getenv(env_var)
    if value:
        return value
    
    prompt = f"{prompt_text} [{default}]: " if default else f"{prompt_text}: "
    
    if password:
        import getpass
        value = getpass.getpass(prompt)
    else:
        value = input(prompt)
    
    return value.strip() if value else default


def main():
    """Main entry point"""
    print("\n" + "=" * 60)
    print(" Zabbix Automation Runner v1.0.0")
    print("=" * 60 + "\n")
    
    check_python_version()
    python_exe = setup_virtualenv()
    install_dependencies(python_exe)
    
    print(f"\n{Colors.OKGREEN}Setup complete!{Colors.ENDC}")
    print("\nExample usage:")
    print("  from zabbix_utils import ZabbixAPI, Sender, Getter")
    print("  api = ZabbixAPI(url='https://zabbix.example.com')")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Cancelled{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}Error: {e}{Colors.ENDC}")
        sys.exit(1)
