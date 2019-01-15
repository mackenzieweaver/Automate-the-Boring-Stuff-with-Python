#! python3
# strongPasswordDetection.py
# 8+ chars long
# Both UPPER and lower case
# 1+ digits

import re
hasCap = re.compile(r'[A-Z]') # capital
hasLow = re.compile(r'[a-z]') # lower
hasNum = re.compile(r'[0-9]') # num

def detectPassword(password):
    if len(password) < 8:
        return False
    if hasCap.search(password) == None:
        return False
    if hasLow.search(password) == None:
        return False
    if hasNum.search(password) == None:
        return False
    else:
        return True
# main
print('Enter a password: ', end = '')
password = input()
if detectPassword(password) == True:
    print('Strong')
else:
    print('Weak')
