# Cybersecurity Tools

## Table of Contents

- [Cybersecurity Tools](#cybersecurity-tools)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Tools](#tools)
    - [Cryptography](#cryptography)
    - [Flooding Attacks](#flooding-attacks)
    - [Password Attacks](#password-attacks)
    - [Scans](#scans)
    - [Web](#web)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [References](#references)
  - [Contact](#contact)

## Introduction

This repository contains a list of cybersecurity tools written mostly in Python. The tools are divided into categories such as cryptography, flooding attacks, password attacks, scans, and web. The tools are meant to be used for educational purposes only.

## Tools

### Cryptography

To be added.

### Flooding Attacks

| Tool | Description | Usage |
| ---- | ----------- | ----- |
| [SYN Flooder](flooding-attacks/syn_flood.py) | A SYN Flooder is a type of DoS attack in which the attacker sends a succession of SYN requests to a target's system in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic. | `python syn_flood.py -t <target_ip> -p <target_port> -c <count>` |
| [ICMP Flooder](flooding-attacks/icmp_flood.py) | An ICMP Flooder is a type of DoS attack in which the attacker sends a succession of ICMP requests (ex. ping) to a target's system in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic. | `python imcp_flood.py -t <target_ip> -c <count>` |
| [Ping of Death](flooding-attacks/ping_of_death.py) | A Ping of Death is a type of DoS attack in which the attacker sends a ping packet larger than the maximum packet size allowed by the IP protocol. | `python ping_of_death.py -t <target_ip>` |
| [Fragmentation Attack](flooding-attacks/fragmentation.py) | A Fragmentation Attack is a type of DoS attack in which the attacker sends a series of fragmented packets to a target's system in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic. | `python fragmentation.py <target_ip> -s <src_ip> -p <port> -i <id> -t <type> -d <data> -f <fragsize>` |
| [DoS Attack](flooding-attacks/Dos.py) | A DoS Attack is a type of attack in which the attacker sends a succession of requests to a target's system in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic. | `python Dos.py -t <target_ip> -c <count>` |
| [DDoS Attack](flooding-attacks/DDoS.py) | A DDoS Attack is a type of attack in which the attacker sends a succession of requests to a target's system from multiple sources in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic. | `python3 DDoS.py -t <target_ip> -c <count> -T <threads>` |

### Password Attacks

| Tool | Description | Usage |
| ---- | ----------- | ----- |
| [SSH](password-attacks/ssh_bruteforce.py) | An SSH Brute Force Attack is a type of attack in which the attacker tries to guess the password of an SSH server by trying different combinations of passwords. | `python3 ssh_bruteforce.py <target> <username> <password_list>` |
| [FTP](password-attacks/ftp_bruteforce.py) | An FTP Brute Force Attack is a type of attack in which the attacker tries to guess the password of an FTP server by trying different combinations of passwords. | `python3 ftp_bruteforce.py <target> <user> <dictionary>` |
| [Telnet](password-attacks/telnet_bruteforce.py) | A Telnet Brute Force Attack is a type of attack in which the attacker tries to guess the password of a Telnet server by trying different combinations of passwords. | `python3 telnet_bruteforce.py <target> <user> <dictionary>` |
| [MySQL](password-attacks/mysql_bruteforce.py) | A MySQL Brute Force Attack is a type of attack in which the attacker tries to guess the password of a MySQL server by trying different combinations of passwords. | `python3 mysql_bruteforce.py <host> <user> <dictionary>` |
| [ZIP](password-attacks/zip_cracker.py) | A ZIP Brute Force Attack is a type of attack in which the attacker tries to guess the password of a ZIP file by trying different combinations of passwords. | `python3 zip-crack.py -f <zipfile> -d <dictionary>` |
| [PDF](password-attacks/pdf_cracker.py) | A PDF Brute Force Attack is a type of attack in which the attacker tries to guess the password of a PDF file by trying different combinations of passwords. | `python3 pdf_cracker.py <pdf_file> <dictionary_file>` |

### Scans

| Tool | Description | Usage |
| ---- | ----------- | ----- |
| [Port Scanner](scanning/port_scanner.py) | A Port Scanner is a tool that scans a target's system for open ports. | `python3 port_scanner.py` |

### Web

| Tool | Description | Usage |
| ---- | ----------- | ----- |
| [Local File Inclusion Tester](web/lfi_test.py) | A Local File Inclusion Tester is a tool that tests a target's system for Local File Inclusion vulnerabilities. | `python3 lfi_test.py -t <URL> -f <Payload File>` |
| [XSS Tester](web/xss_tester.py) | A XSS Tester is a tool that tests a target's system for Cross-Site Scripting vulnerabilities. | `python3 XSS_tester.py -u <URL> -f <Payload File>` |

## Contributing

If you would like to contribute to this repository, please open an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Python](https://www.python.org/)
- [Scapy](https://scapy.net/)
- [Requests](https://docs.python-requests.org/en/master/)
- [Argparse](https://docs.python.org/3/library/argparse.html)
- [Sys](https://docs.python.org/3/library/sys.html)

### References

- [LFI Payloads](https://github.com/emadshanab/LFI-Payload-List) : Emad Shanab
- [XSS Payloads](https://github.com/payloadbox/xss-payload-list) : PayloadBox

## Contact

If you want to contact me you can reach me at [cherifjebali0301@gmail.com](mailto:cherifjebali0301@gmail.com).
