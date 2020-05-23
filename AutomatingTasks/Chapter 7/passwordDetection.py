#! python3

#This script should take the input from the user and then check for strength

import pyperclip, re

#TODO: Get up strong Password Regex Tests
alphaRegex = re.compile(r'[a-z]')
alphaCapitalRegex = re.compile(r'[A-Z]')
numRegex = re.compile(r'[0-9]')

#TODO: Get password
password = str(pyperclip.paste())




#TODO: Define a "Strong" Password




# TODO: Check that password is strong







#TODO: Tell User if the password is indeed strong