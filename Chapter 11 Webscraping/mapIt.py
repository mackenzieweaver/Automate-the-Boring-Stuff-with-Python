#! python3
# mapIt.py
# Launches a map in the browser using an address
# from the command line or clipboard

import webbrowser, sys, logging, pyperclip


if len(sys.argv) > 1:
    # From command line
    address = ' '.join(sys.argv[1:])
else:
    # From clipboard
    address = pyperclip.paste()
# Open browser
webbrowser.open('https://www.google.com/maps/place/' + address)
