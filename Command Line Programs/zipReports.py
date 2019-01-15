#! python3
# selectiveCopy.py - Copies certain files into a new folder

import os, shutil, datetime, zipfile, re, pprint, send2trash

record = re.compile(r'(\s*)?( - ESL Record )(\d).doc')
        
now = datetime.datetime.now()
date = (str(now.month) + '.' +
        str(now.day)   + '.' +
        str(now.year))

# New folder
os.chdir('C:\\Users\\Mack W\\Desktop\\English Steward')
dest = os.getcwd()
    
# Zip file
reports = zipfile.ZipFile('Reports_%s' % date + '.zip', 'w')
walk = 'C:\\Users\\Mack W\\Desktop\\English Steward\\1 Students'

# Walk the folder's tree
totalsize = 0
for folderName, subfolders, filenames in os.walk(walk):
    for filename in filenames:
        if record.search(filename) != None:
            src = os.path.join(folderName, filename)
            shutil.copy(src, dest)
            size = os.path.getsize(filename)
            totalsize += size
            reports.write(filename, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(filename)
            
# Print and close
#pprint.pprint(reports.namelist())
#print(totalsize)
reports.close()
