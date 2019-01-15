#! python3
#An insecure password locker program
"""
Master password unlocks manager
Copy account password to clipboard
Paste into website
Run with command line
"""

PASSWORDS = {'email': 'aldskfasfnahALK1982376',
             'blog': 'VSKJDFjsaldkfafn129382',
             'luggage': '12345'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
