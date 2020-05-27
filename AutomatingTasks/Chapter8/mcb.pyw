#! pyhton3
# mcb.pyw - saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
