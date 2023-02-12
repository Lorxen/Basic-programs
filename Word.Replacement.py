def replace_word():

    phrase = input('Please enter the text you want to change: ')
    word_to_replace = input('Please enter the word you want to replace: ')
    word_replacement = input('Please enter the word replacement: ')
    print(phrase.replace(word_to_replace, word_replacement))

replace_word()