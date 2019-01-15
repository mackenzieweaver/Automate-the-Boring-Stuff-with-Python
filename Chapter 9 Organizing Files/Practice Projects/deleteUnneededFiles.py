#! python3
# deleteUnnededFiles.py
# lists files in a directory that are greater than 100MB
import os, pprint
print('Search: ', end='')
directory = input()
print('Size (MB): ', end='')
size = input()
for foldername, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        path = os.path.join(foldername, filename)
        bytesize = os.path.getsize(path)
        kbsize = bytesize / 1000
        mbsize = kbsize / 1000
        if int(mbsize) > int(size):
            print(path)
            print(str(int(mbsize)) + 'MB')
