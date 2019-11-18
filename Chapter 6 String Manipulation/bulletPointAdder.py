#! python3

#This program will add Wikipedia bullets to the front of all lines of text in the clipboard

import pyperclip 
text = pyperclip.paste()

#TODO Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)

