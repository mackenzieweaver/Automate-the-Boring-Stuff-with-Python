#! python3
# regexSearch.py
import os, re, pprint

# user path
print('Location: ', end = '')
directory = input()
os.chdir(directory)

# all files in directory
dirList = os.listdir()  

# user expression to search
print('Search: ', end='')
expression = input()

# regular expressions
string = re.compile(expression)
textFileType = re.compile(r'.+\.(txt)|(TXT)$')  

# open all .txt files in a folder
for i in range(len(dirList)):
    # check if it's a text file
    if textFileType.search(dirList[i]) == None:
        continue

    textFile = open(dirList[i], 'r')
    
    # print file name
    print('File: ' + os.path.basename(dirList[i]).ljust(28), end='')    
    
    # read each file
    content = textFile.readlines()
    
    # read each line
    lines = []
    for j in range(len(content)):
        # search each line
        mo = string.search(content[j])
        # save line number into a list
        if mo:
            lines += [(j + 1)]
            
    # print line where the expression is found
    if len(lines) > 1:
        print('Lines: '.rjust(12), end='')
        for k in range(len(lines)-1):
            print(lines[k], end=', ')
        print(lines[len(lines)-1])
    elif len(lines) == 1:
        print('Line: '.rjust(12) + str(lines[0]))
    else:
        print('No matches'.rjust(11))

# always close your files :)
textFile.close()








