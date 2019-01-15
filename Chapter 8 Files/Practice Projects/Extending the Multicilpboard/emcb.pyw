#! python3
# mcb.pyw - multiclipboard
#        0         1         2
# emcb.pyw      save <keyword> - saves clipboard to keyword
# emcb.pyw    delete <keyword> - deletes keyword
# emcb.pyw    delall           - deletes all keywords
# emcb.pyw      list           - loads list of keywords to clipboard
# emcb.pyw <keyword>           - loads keyword contents to clipboard
import shelve, pyperclip, sys
#                        file
emcbShelf = shelve.open('emcb')
if len(sys.argv) == 3:
    # Save clipboard to keyword
    if sys.argv[1].lower() == 'save':
        emcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete a keyword from the shelf
    elif sys.argv[1].lower() == 'delete':
        del emcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # Delete all keywords
    if sys.argv[1].lower() == 'delall':
        for k in emcbShelf:
            del emcbShelf[k]
    # List keywords and load content
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(emcbShelf.keys())))
    # Copy keyword string to keyboard
    elif sys.argv[1] in emcbShelf:
        pyperclip.copy(emcbShelf[sys.argv[1]])
emcbShelf.close()
