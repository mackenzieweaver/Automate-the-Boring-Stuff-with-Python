#! python3
# selectiveCopy.py - Copies certain files into a new folder

import os, shutil

# Folder
print('Search folder: ', end='')
search = input()

# Type of files to copy
print('Type of file: ', end='')
fileType = input()

# New folder
print('Destination: ', end='')
destination = input()
if not os.path.exists(destination):
    os.mkdir(destination)

# Walk the folder's tree
for folderName, subfolders, filenames in os.walk(search):
    #print(folderName, subfolders, filenames)
    for filename in filenames:
        if filename.endswith(fileType):
            src = os.path.join(folderName, filename)
            dest = os.path.abspath(destination)
            shutil.copy(src, dest)
