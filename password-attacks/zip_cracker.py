# Cracks a password protected zip file using a dictionary attack
# Usage: python zip-crack.py -f <zipfile> -d <dictionary>

import zipfile
import argparse

def main(zipfilename, dictionary):
    """
    Zipfile password cracker using a brute-force dictionary attack
    """
    password = None # Initialize password to None 
    zip_file = zipfile.ZipFile(zipfilename) # Open the zip file
    passwords = open(dictionary, 'r').readlines() # Read the dictionary file
    for p in passwords: 
        password = p.strip('\n') # Strip the newline character
        try:
            zip_file.extractall(pwd=password) # Try to extract the zip file with the password
            print ('Password found: %s' % password) # If successful, print the password
        except: 
            pass # If not successful, pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Cracks a password protected zip file using a dictionary attack")  # Create a parser object
    parser.add_argument("-f", dest="zipfilename", type=str, help="Specify a zip file")  # Add an argument to the parser
    parser.add_argument("-d", dest="dictionary", type=str, help="Specify a dictionary file") # Add an argument to the parser
    args = parser.parse_args() # Parse the arguments
    zipfilename = args.zipfilename # Assign the zip file to the variable zipfilename
    dictionary = args.dictionary # Assign the dictionary file to the variable dictionary
    main(zipfilename, dictionary)