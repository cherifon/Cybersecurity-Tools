# Usage: python3 lfi_test.py -t <URL> -f <Payload File>

import requests
import argparse

def load_payloads(file_path):
    """
    Load LFI payloads from a local file with robust encoding handling.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            payloads = [line.strip() for line in file.readlines() if line.strip()]
        print(f"[+] Loaded {len(payloads)} payloads from {file_path}.")
        return payloads
    except UnicodeDecodeError:
        print("[!] Failed to decode file with utf-8. Retrying with latin1...")
        try:
            with open(file_path, 'r', encoding='latin1') as file:
                payloads = [line.strip() for line in file.readlines() if line.strip()]
            print(f"[+] Loaded {len(payloads)} payloads from {file_path} using latin1.")
            return payloads
        except Exception as e:
            print(f"[-] Error reading file {file_path} with latin1: {e}")
            return []
    except FileNotFoundError:
        print(f"[-] File not found: {file_path}")
        return []
    except Exception as e:
        print(f"[-] Error reading file {file_path}: {e}")
        return []


def test_lfi(target_url, payloads):
    """
    Test the target URL with each LFI payload.
    """
    for payload in payloads:
        if not target_url.endswith('='):
            # Ensure proper URL construction
            full_url = f"{target_url}?file={payload}"  # Adjust parameter name if needed
        else:
            full_url = f"{target_url}{payload}"

        try:
            response = requests.get(full_url, timeout=5)

            # Detection logic
            if "root:x:" in response.text or "bin/bash" in response.text or "Windows" in response.text: # If the response contains a string that indicates a successful LFI
                print(f"[!] Potential LFI detected: {full_url}")
        except requests.RequestException as e:
            print(f"[-] Request failed for {full_url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="LFI Vulnerability Tester")
    parser.add_argument("-t", "--target", required=True, help="Target URL (e.g., http://example.com/index.php?page=).")
    parser.add_argument("-f", "--file", required=False, help="Path to the local file containing LFI payloads.", default="LfiPayloads.txt")
    args = parser.parse_args()

    print("[+] Loading payloads...")
    payloads = load_payloads(args.file)

    if payloads:
        print("[+] Starting LFI tests...")
        test_lfi(args.target, payloads)
    else:
        print("[-] No payloads to test.")

if __name__ == "__main__":
    main()
