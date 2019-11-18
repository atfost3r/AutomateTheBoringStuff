#! python3
#This is an insecure password Locker

PASSWORDS = {'email': 'WHATAREYOUDOINGLOOKINGATMYEMAIL',
             'website': '123456789101112131415',
             'bank': '$1BILLION'  }

import sys.pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named' + account)