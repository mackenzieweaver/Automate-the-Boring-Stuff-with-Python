#! python3
# regexStrip.py
# Regular expression version of the strip() method
# Two arguments: string, characters to remove

import re
space = re.compile(r'(^\s+)(.*?)(\s+$)')
def regexStrip(string, chars = ''):
    if len(chars):
        remove = re.compile(r'[' + chars + ']')
        print(remove.sub('', string))
    else:
        print(space.search(string).group(2))
regexStrip('     This is a string     ', 's')
