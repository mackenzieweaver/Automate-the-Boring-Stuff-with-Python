#! python 3
# madLibs2.py
import os, re
replace = []

# Open file
inputFile = open(r'C:\Users\Mack W\Documents\7 Python\pyFiles\Automate the Boring Stuff with Python\Chapter 8 Files\Practice Projects\MadLibsPrompt.txt')
fileContent = inputFile.read()

# Find ADJECTIVE, NOUN, ADVERB, or VERB
grammar = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
gmo = grammar.findall(fileContent)
for i in range(len(gmo)):
   if gmo[i] == 'ADJECTIVE':
      print('Enter an adjective:')
      fileContent = fileContent.replace('ADJECTIVE', input(), 1)
   else:
      print('Enter a ' + gmo[i].lower() + ':')
      fileContent = fileContent.replace(gmo[i], input(), 1)
print(fileContent)

# Create text file with replacements
outputFile = open('newMadLibsPrompt.txt', 'w')
outputFile.write(fileContent)

# Always close your files :)
inputFile.close()
outputFile.close()
