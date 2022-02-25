""" Count Capital Letters
write a one-liner that will count the number of capital letters in a file. """

import re

print("The file contains " + str(len(re.findall(r'[A-Z]', open("letters.txt", "r", encoding="UTF-8").read()))) + " capital letters")
