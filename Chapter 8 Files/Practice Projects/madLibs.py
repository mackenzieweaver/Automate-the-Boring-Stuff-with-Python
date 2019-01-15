#! python 3
# madLibs.py
import os, re

# Open file
textFile = open(r'C:\Users\Mack W\Documents\7 Python\pyFiles\Automate the Boring Stuff with Python\Chapter 8 Files\Practice Projects\madLibsPrompt.txt')

# Find ADJECTIVE, NOUN, ADVERB, and VERB in the file
grammar = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
matchObject = grammar.findall(textFile.read())

# Prompt user to replace them
for i in range(len(matchObject)):
    if matchObject[i] == 'ADJECTIVE':
        print('Enter an adjective: ', end = '')
        adjective += [input()]            
    elif matchObject[i] == 'NOUN':
        print('Enter a noun: ', end = '')
        noun += [input()]
    elif matchObject[i] == 'ADVERB':
        print('Enter an adverb: ', end = '')
        adverb += [input()]
    elif matchObject[i] == 'VERB':
        print('Enter a verb: ', end = '')
        verb += [input()]
        
print(adjective)
print(noun)
print(verb)

# Create text file with replacements

# Always close your files :)
textFile.close()
