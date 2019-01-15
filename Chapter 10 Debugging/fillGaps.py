#! python3
# fillGaps.py
# list txt files in a folder
# that end with number pattern (Ex: 001, 002, 003)
# if number is missing
# rename files
import os, re

# change path
path = 'C:\\Users\\Mack W\\Documents\\Python\\automateTheBoringStuffWithPython\\Chapter 9 Organizing Files\\Practice Projects\\txt'
os.chdir(path)
dirlist = os.listdir()

# regular expression
prefix = re.compile(r'^(spam)(\d){0,3}(.txt)$')

# function 1 
def createfiles():
    # choose number of files to create
    for i in range(10):
        # name it 'spam' plus a number + .txt
        txtfile = open('spam%03d.txt' % i, 'w')
        txtfile.close()

# function 2         
def fillgaps():
    # checks each file
    for i in range(len(dirlist)):
        # checks file against the regular expression
        mo = prefix.search(dirlist[i])
        # if there's no match, go to the next file
        if mo == None:
            continue
        # if the current file doesn't have the 'next number'
        if int(mo.group(2)) != i:
            # then rename it with the next number
            newname = mo.group(1) + ('%03d' % i) + mo.group(3)
            os.rename(dirlist[i], newname)

# function 3
def insertgaps():
    # have user choose where to insert the gap
    print('New file at: ', end='')
    newfile = int(input())
    # times = number of files minus where to insert file
    for i in range((len(dirlist))-newfile):
        # start at the end of the list
        j = len(dirlist)-i-1
        # check last file and work up (towards 000)
        mo = prefix.search(dirlist[j])
        # just add one to each file to 'create' a gap
        newnum = (int(mo.group(2)) + 1)
        newname = mo.group(1) + ('%03d' % newnum) + mo.group(3)
        # Thank you os method for having a rename feature
        os.rename(dirlist[j], newname)
    
# main - uncomment a function to use it
#createfiles()
#fillgaps()
#insertgaps()
