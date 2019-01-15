#! python3
# mcb.pyw - multiclipboard

# py mcb.pyw save <keyword> - saves clipboard to keyword
# py mcb.pyw <keyword>      - loads keyword to clipboard
# py mcb.pyw                - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')    

# TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
