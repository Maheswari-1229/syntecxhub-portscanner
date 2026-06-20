# Advanced TCP Port Scanner

## Project Overview

The Advanced TCP Port Scanner is a Python-based network security tool designed to identify open TCP ports on a target host. It uses socket programming and multithreading to perform fast and efficient port scanning while providing detailed scan results.

This project was developed as part of a cybersecurity internship to demonstrate networking concepts, TCP communication, service enumeration, exception handling, and secure coding practices.

## Features

* TCP Port Scanning
* Custom Port Range Selection
* Multi-threaded Scanning for Faster Performance
* Service Detection for Common Ports
* Banner Grabbing Support
* Scan Result Logging
* Exception Handling
* Scan Statistics Summary
* Timestamp-Based Report Generation
* Hostname to IP Resolution

## Technologies Used

* Python 3
* Socket Programming
* Threading
* Datetime Module
* File Handling
* Network Security Fundamentals

## Installation

### Clone the Repository

```bash
git clone https://github.com/Maheswari-1229/syntecxhub-portscanner.git
```

### Navigate to Project Directory

```bash
cd syntecxhub-portscanner
```

### Verify Python Installation

```bash
python --version
```

Python 3.x or higher is recommended.

## Usage

Run the scanner using:

```bash
python portscanner.py
```

Enter:

* Target IP Address or Domain Name
* Starting Port
* Ending Port

Example:

```text
Enter Target IP or Domain: scanme.nmap.org
Enter Start Port: 1
Enter End Port: 1000
```

The scanner will:

* Resolve the hostname
* Scan the specified port range
* Display open ports
* Detect common services
* Save results to a timestamped report file

## Sample Output

```text
============================================================
ADVANCED TCP PORT SCANNER
============================================================

Target: scanme.nmap.org
IP Address: 45.33.32.156

[OPEN] Port 22    Service: SSH
[OPEN] Port 80    Service: HTTP

============================================================
SCAN COMPLETED
============================================================

Open Ports Found: 2
Closed Ports: 998
Timeout Ports: 0

Results saved to:
scan_20260620_173001.txt
```

## Project Structure

```text
syntecxhub-portscanner/
│
├── portscanner.py
├── README.md
├── .gitignore
└── scan_YYYYMMDD_HHMMSS.txt
```

## Future Enhancements

* UDP Port Scanning
* CIDR Range Scanning
* OS Fingerprinting
* Vulnerability Detection
* CVE Lookup Integration
* CSV Export
* PDF Report Generation
* GUI Interface using Tkinter
* Real-Time Progress Bar
* Network Discovery Module

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Socket Programming
* TCP Networking
* Multithreading
* Network Reconnaissance
* Service Enumeration
* Error Handling
* Python Development
* Cybersecurity Fundamentals

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Users must obtain proper permission before scanning any system, network, or host. Unauthorized scanning of third-party systems may violate laws, regulations, or organizational policies.

The developer is not responsible for any misuse of this tool.
