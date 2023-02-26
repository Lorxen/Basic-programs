# Have a python dictionary that has a key/value pair that represents a word and its definition
# Collect input from the user input is a word
# Check if the word id in the dictionary
# Print the definition

from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:

    word = input('Enter your word: ')
    if word == '':
        break
    print(dictionary.printMeanings(word))
