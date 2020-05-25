#! python3

#This script should take the input from the user and then check for strength

import pyperclip, re

#TODO: Get up strong Password Regex Tests
alphaRegex = re.compile(r'[a-z]')
alphaCapitalRegex = re.compile(r'[A-Z]')
numRegex = re.compile(r'[0-9]')

#TODO: Get password
password = str(pyperclip.paste())
strong = [0,0,0]

# TODO: Check that password is strong
if len(password) >= 8:
    if alphaRegex.findall(password) == []:

        print(password)


else:




#TODO: Define a "Strong" Password





#TDOD: Tell the user that their password sucks or not
print('This is one strong password')

#TODO: Tell User if the password is indeed strong