# Cracks a PDF password using a dictionary attack
# Usage: python pdf_cracker.py <pdf_file> <dictionary_file>

import PyPDF2
import sys

def crack_pdf(file, dictionary):
    pdf_reader = PyPDF2.PdfFileReader(file) # Open the PDF file
    with open(dictionary, 'r') as f: 
        for line in f:
            password = line.strip() # Remove leading/trailing whitespaces
            if pdf_reader.decrypt(password) == 1: # Try to decrypt the PDF
                print(f'Password found: {password}') # Print the password
                break
        else:
            print('Password not found') # Print if the password is not found

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python pdf_cracker.py <pdf_file> <dictionary_file>')
    else:
        crack_pdf(sys.argv[1], sys.argv[2])
