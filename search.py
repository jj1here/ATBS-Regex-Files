#!python3
#takes an input and searches the .txt files in the current directory for the word

import re, os
from pathlib import Path

# word to search for
find = input("What word would you like to find?\n")
# gets current directory
p = Path.cwd()

# for regex express
searchFor = re.compile(rf"{find}")

# collects the files with the word
found = []

# loops through the files
for file in p.glob('*.txt'):
    openFile = open(file,'r') #opens the file
    readFile = openFile.read() #reads the file
    mo = searchFor.search(readFile) #searchs the file for the word
    if mo != None : #if one instance found the file is added to found
        found.append(os.path.basename(file))

final = " ".join(found) #seprates the files by a space
if len(found) > 0: #if a file was found
    print(f"{find} was found in {final}")
else: #if a file was not found
    print(f"Sorry I couldn't find {find}")


