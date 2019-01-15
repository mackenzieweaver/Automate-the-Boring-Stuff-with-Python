#! python3
# splitPdf.py - big pdf -> some pages of that pdf
# inputs: pdf file location, new name, new destination
# outputs: new pdf with new name in new destination

import PyPDF2, os, sys, pprint

# Example
path = 'C:\\Users\\Mack W\\Desktop\\English Steward\\Materials'

# Brand
print(path)
os.chdir(path)
pprint.pprint(os.listdir())
choice = input()
path = os.path.join(path, choice)

# Subject
print(path)
os.chdir(path)
pprint.pprint(os.listdir())
choice = input()
path = os.path.join(path, choice)

# Grade
print(path)
os.chdir(path)
pprint.pprint(os.listdir())
choice = input()
path = os.path.join(path, choice)

# File
print(path)
os.chdir(path)
pprint.pprint(os.listdir())
choice = input()
path = os.path.join(path, choice)

# Example      
print('Save to: ', end='')
nameDate = input()
dest = 'C:\\Users\\Mack W\\Desktop\\English Steward\\Students\\' + nameDate
if os.path.exists(dest) == False:
    os.makedirs(dest, exist_ok=True)

# Page numbers
print('Number of pages: ', end='')
numOfPages = int(input())

print('Starting from: ', end='')
pageNum = int(input()) - 1

# open file in read binary mode
pdf = open(path, 'rb')
# pdf file reader object
reader = PyPDF2.PdfFileReader(pdf)
# pdf file writer object
writer = PyPDF2.PdfFileWriter()

for i in range(numOfPages):
    # read page
    page = reader.getPage(pageNum + i)
    # write page
    writer.addPage(page)

# output
os.chdir(dest)
outputFile = open('Material.pdf', 'wb')
writer.write(outputFile)

# close files
outputFile.close()
pdf.close()

