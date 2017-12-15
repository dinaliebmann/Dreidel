'''
Returns all English words of a given length with the provided characters, a tool for finding
possible words to fit in a crossword (as a crossword creator or solver).
Note: This only returns single words, so any clues with two or more words will not be returned.

This corpus is not a complete collection of all words. Some results may be repeated, and some
may not be listed (especially pluralized words)
'''

from nltk.corpus import words

def possibilities():
    # Obtain list of English words from NLTK
    wordlist = words.words()

    # Word information from user input
    letters = input("Write all the letters you know. For any letters you don't know, write X "
                    "in their place.\nFor example, if the word is 'hello' and you have the 'el' and 'o', you "
                    "would write 'XelXo'\nEnter the word: ")
    word_len = len(letters)

    # Determine the possible words
    possibilities = [word for word in wordlist if len(word) == word_len]
    for i in range(word_len):
        if letters[i] is not 'X':
            possibilities = [word for word in possibilities if word[i] == letters[i]]

    return possibilities
