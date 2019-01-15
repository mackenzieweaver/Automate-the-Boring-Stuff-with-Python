#! python 3
# madLibs2.py
import os, re

# Open file
inputFile = open(r'C:\Users\Mack W\Documents\7 Python\pyFiles\Automate the Boring Stuff with Python\Chapter 8 Files\Practice Projects\MadLibsPrompt.txt')
fileContent = inputFile.read()

# Find ADJECTIVE, NOUN, ADVERB, or VERB
grammar = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
gmo = grammar.search(fileContent)
while gmo != None:   
   gmo = gmo.group().lower()
   if gmo == 'adjective' or gmo == 'adverb':
      print('Enter an ' + gmo + ':')
   else:
      print('Enter a ' + gmo + ':')      
   fileContent = grammar.sub(input(), fileContent, 1)
   gmo = grammar.search(fileContent)
print(fileContent)

# Create text file with replacements
outputFile = open(r'C:\Users\Mack W\Documents\7 Python\pyFiles\Automate the Boring Stuff with Python\Chapter 8 Files\Practice Projects\anotherNewMadLibsPrompt.txt', 'w')
outputFile.write(fileContent)

# Always close your files :)
inputFile.close()
outputFile.close()
