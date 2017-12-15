'''
Returns all English words of a given length with the provided characters, a tool for finding
possible words to fit in a crossword (as a crossword creator or solver).
Note: This only returns single words, so any clues with two or more words will not be returned.
'''

from nltk.corpus import words

def possibilities():
    wordlist = words.words()
    word_len = int(input("Length of the word: "))
    assert(word_len >= 2)
    letters = input("Write all the letters you know. For any letters you don't know, write X.\n"
                    "For example, if the word is 'hello' and you have the 'el' and 'o', you would write 'XelXo'\n"
                    "Enter the word: ")
    possibilities = [word for word in wordlist if len(word) == word_len]
    if letters[0] is not 'X':
        possibilities = [word for word in possibilities if word[0] == letters[0]]
    if letters[1] is not 'X':
        possibilities = [word for word in possibilities if word[1] == letters[1]]
    if word_len >= 3 and letters[2] is not 'X':
        possibilities = [word for word in possibilities if word[2] == letters[2]]
    if word_len >= 4 and letters[3] is not 'X':
        possibilities = [word for word in possibilities if word[3] == letters[3]]
    if word_len >= 5 and letters[4] is not 'X':
        possibilities = [word for word in possibilities if word[4] == letters[4]]
    if word_len >= 6 and letters[5] is not 'X':
        possibilities = [word for word in possibilities if word[5] == letters[5]]
    if word_len >= 7 and letters[6] is not 'X':
        possibilities = [word for word in possibilities if word[6] == letters[6]]
    if word_len >= 8 and letters[7] is not 'X':
        possibilities = [word for word in possibilities if word[7] == letters[7]]
    if word_len >= 9 and letters[8] is not 'X':
        possibilities = [word for word in possibilities if word[8] == letters[8]]
    if word_len >= 10 and letters[9] is not 'X':
        possibilities = [word for word in possibilities if word[9] == letters[9]]
    if word_len >= 11 and letters[10] is not 'X':
        possibilities = [word for word in possibilities if word[10] == letters[10]]
    if word_len >= 12 and letters[11] is not 'X':
        possibilities = [word for word in possibilities if word[11] == letters[11]]
    if word_len >= 13 and letters[12] is not 'X':
        possibilities = [word for word in possibilities if word[12] == letters[12]]
    if word_len >= 14 and letters[13] is not 'X':
        possibilities = [word for word in possibilities if word[13] == letters[13]]
    return possibilities
