"""
Create texts based on the user input
"""

#Importing random and string module
import random,string

#Defining the vowel and consonants
vowels = "aeiouy"
letters =  string.ascii_lowercase
consonants = letters

for c in vowels:
    consonants = consonants.replace(c,"")

#User inputs
word_length = input("Enter number of letters should be in the word: ")
word_range = input("Enter number of words needed: ")

#Defining a list to store the letters of the words
lst = []
for i in range(int(word_length)):
    lst.append(input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter or any letter in specific: "))

#Generate the word
def generator(lst):
    word  = ""
    for s in lst:
        if(s == "v"):
            word = word + random.choice(vowels)
        elif(s=="c"):
            word = word + random.choice(consonants)
        elif(s=="l"):
            word = word + random.choice(letters)
        else:
            word = word + s
    return(word)

#Defining a list to store different words
word_list = []
for word in range(int(word_range)):
    word_list.append(generator(lst))

#Priting all words
for word in word_list:
    print(word)
