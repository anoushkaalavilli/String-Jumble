"""
stringjumble.py
Author: Eric
Credit: Me!

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
# Anoushka Alavilli
# Credits: 1) http://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string 
# Credits: 2) http://www.dotnetperls.com/split-python

text= input("Please enter a string of text (the bigger the better): ")
print ("You entered " + (str(text)) + ". Now jumble it: ")

# makes everything backwards
listtext= list(str(text))
print (''.join(listtext[::-1]))

# makes words but not letter backwards
strtext= (str(text)).split(" ")
print (' '.join(strtext[::-1]))

# makes letters but not words backwards
strtext= (str(text)).split(" ")
print (i[::-1])











