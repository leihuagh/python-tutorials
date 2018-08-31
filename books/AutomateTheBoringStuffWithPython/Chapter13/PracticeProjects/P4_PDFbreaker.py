# Say you have an encrypted PDF that you have forgotten the password to, but you
# remember it was a single English word. Trying to guess your forgotten password
# is quite a boring task. Instead you can write a program that will decrypt the
# PDF by trying every possible English word until it finds one that works.
#
# Create a list of word strings by reading dictionary.txt. Then loop over each word in
# this list, passing it to the decrypt() method. If this method returns the integer
# 0, the password was wrong and your program should continue to the next password.
# If decrypt() returns 1, then your program should break out of the loop and print
# the hacked password. You should try both the uppercase and lowercase form of
# each word.
#
# Note:
# - Dictionary text file can be downloaded from http://nostarch.com/automatestuff/

import PyPDF4

FILE = "../allminutes_encrypted.pdf"

# Get dictionary
with open("dictionary.txt") as file:
    words = file.read().splitlines()

# Load encrypted PDF
pdfReader = PyPDF4.PdfFileReader(open(FILE, "rb"))
if not pdfReader.isEncrypted:
    print("FileError: PDF is not encrypted")
    raise RuntimeError

# Try each word in dictionary (upper and lower case)
for word in words:
    # Print password, if found
    if pdfReader.decrypt(word) or pdfReader.decrypt(word.lower()):
        print("The password is either %s or %s" % (word, word.lower()))
        break
    else:
        continue
if word == words[-1]:
    print("Failed to break PDF.")
