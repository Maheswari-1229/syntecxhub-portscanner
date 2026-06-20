import socket
import threading
from datetime import datetime

print("=" * 60)
print("          ADVANCED TCP PORT SCANNER")
print("=" * 60)

target = input("Enter Target IP or Domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("[-] Invalid Hostname")
    exit()

start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print(f"\n[+] Target: {target}")
print(f"[+] IP Address: {target_ip}")
print(f"[+] Scanning Ports: {start_port} - {end_port}")

start_time = datetime.now()

open_ports = []
closed_ports = []
timeout_ports = []

lock = threading.Lock()

services = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    80: "HTTP",
    110: "POP3",
    111: "RPC",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Proxy"
}

from datetime import datetime

result = f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

log_file = open(result, "w")
log_file.write("ADVANCED TCP PORT SCANNER REPORT\n")
log_file.write("=" * 60 + "\n")
log_file.write(f"Target: {target}\n")
log_file.write(f"IP Address: {target_ip}\n")
log_file.write(f"Port Range: {start_port}-{end_port}\n")
log_file.write(f"Scan Started: {start_time}\n\n")


def grab_banner(sock):
    try:
        sock.settimeout(2)
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return "No Banner"


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service = services.get(port, "Unknown")

            banner = grab_banner(sock)

            with lock:
                open_ports.append(port)

                output = (
                    f"[OPEN] Port {port:<5} "
                    f"Service: {service:<15} "
                    f"Banner: {banner}"
                )

                print(output)
                log_file.write(output + "\n")

        else:
            with lock:
                closed_ports.append(port)

        sock.close()

    except socket.timeout:
        with lock:
            timeout_ports.append(port)

    except Exception:
        pass


threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = datetime.now()
duration = end_time - start_time

print("\n" + "=" * 60)
print("SCAN COMPLETED")
print("=" * 60)

print(f"Target: {target}")
print(f"Open Ports Found: {len(open_ports)}")
print(f"Closed Ports: {len(closed_ports)}")
print(f"Timeout Ports: {len(timeout_ports)}")
print(f"Duration: {duration}")

log_file.write("\n")
log_file.write("=" * 60 + "\n")
log_file.write("SCAN SUMMARY\n")
log_file.write("=" * 60 + "\n")
log_file.write(f"Open Ports: {len(open_ports)}\n")
log_file.write(f"Closed Ports: {len(closed_ports)}\n")
log_file.write(f"Timeout Ports: {len(timeout_ports)}\n")
log_file.write(f"Scan Duration: {duration}\n")

log_file.close()

print("\nResults saved to " + result)