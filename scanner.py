import socket
import nmap

def scan_target(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-T4 -F')

    if target not in nm.all_hosts():
        print(f"❌ No results found for {target}.")
        return []

    results = []
    for proto in nm[target].all_protocols():
        for port in nm[target][proto].keys():
            state = nm[target][proto][port]['state']
            banner = grab_banner(target, port)
            results.append({'port': port, 'state': state, 'banner': banner})
    return results

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return "N/A"
