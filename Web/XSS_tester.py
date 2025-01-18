# Usage : python3 XSS_tester.py -u <URL> -f <Payload File>

import requests
import sys
import re # Regular Expression
import argparse

def test_xss(url, payload_file):
    print("Your target url should be like http://example.com/search?q=")
    
    vulnerable = []
    f = open(payload_file, "r")
    for payload in f.read().splitlines(): # splitlines() split the string at line breaks and returns a list of lines in the string
        link = url + payload  # Concatenation of the url and the payload
        r = requests.get(link) # Send a GET request to the specified URL
        if payload.lower() in r.text.lower(): # Check if the payload is in the response text
            print("[-] This site is vulnerable to: " + payload)

            if payload not in vulnerable: # Check if the payload is not already in the list
                vulnerable.append(payload) # Add the payload to the list
            else:
                pass
        else:
            pass
    f.close()

    print("[-] Available payloads:") 
    print("\n".join(vulnerable)) # Print the list of vulnerable payloads

def main():
    parser = argparse.ArgumentParser(description="XSS Tester")
    parser.add_argument("-u", "--url", help="Target URL", required=True)
    parser.add_argument("-f", "--file", help="Payload File", required=False, default="XssPayloads.txt")
    args = parser.parse_args()

    test_xss(args.url, args.file)

if __name__ == "__main__":
    main()