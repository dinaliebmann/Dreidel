'''
Returns all English words of a given length with the provided characters, a tool for finding
possible words to fit in a crossword (as a crossword creator or solver).
Note: This only returns single words, so any clues with two or more words will not be returned.

This corpus is not a complete collection of all words, but is extensive with over 466k words.
'''
# import unittest
# import mock

def crossposs(letters=None):
    with open("words.txt") as word_file:
        wordlist = set(word.strip().lower() for word in word_file)
    
    # Word information from user input
    if letters is None:
        letters = input("Write all the letters you know. For any letters you don't know, write X "
                        "in their place.\nFor example, if the word is 'hello' and you have the 'el' and 'o', you "
                        "would write 'XelXo'\nEnter the word: ")
    word_len = len(letters)

    # Determine the possible words
    possibilities = [word for word in wordlist if len(word) == word_len]
    for i in range(word_len):
        if letters[i] is not 'X':
            possibilities = [word for word in possibilities if word[i] == letters[i].lower()]

    possibilities.sort()
    return possibilities



# # Unit test crossposs
# class TestCrossposs(unittest.TestCase):

#     def test_output_given_input(self):
#         # Checks that when an argument is passed in, it returns something
#         self.assertIsNotNone(crossposs('tesXXng'))
        
#     def test_output_no_input(self):
#         # Checks that when an argument is not passed in, it returns something
#         with mock.patch('builtins.input', return_value='tesXXng'):
#             self.assertIsNotNone(crossposs())
    
#     def test_equal_output(self):
#         # Checks that what is returned is equal no matter how it is passed in
#         # Only one result
#         with mock.patch('builtins.input', return_value='tesXXng'):
#             self.assertEqual(crossposs(), crossposs('tesXXng'))
#         # Many results
#         with mock.patch('builtins.input', return_value='aXeX'):
#             self.assertEqual(crossposs(), crossposs('aXeX'))

#     def test_caps(self):
#         # Checks that entering capitals still works
#         self.assertEqual(crossposs('CXPXTXL'), ['capital', 'capitol'])
    
#     def test_non_letter(self):
#         # Checks that entering a non-letter doesn't return anything or break anyhing
#         self.assertEqual(crossposs('wo$$'), [])
#         self.assertEqual(crossposs('XiñatX'), [])
#         self.assertEqual(crossposs('#'), [])
#         self.assertEqual(crossposs('D@'), [])
#         self.assertEqual(crossposs('123'), [])
        
#     def test_empty_input(self):
#         self.assertEqual(crossposs(''), [])
        
#     def test_noX(self):
#         self.assertEqual(crossposs('word'), ['word'])
#         self.assertEqual(crossposs('ileugbaweig'), [])
        
#     def test_allX(self):
#         self.assertEqual(crossposs('XXXXXXXXXXXXXXXXXXXXXXXXX'), 
#                          ['antidisestablishmentarian', 'demethylchlortetracycline',
#                           'electroencephalographical', 'immunoelectrophoretically',
#                           'microspectrophotometrical', 'philosophicopsychological',
#                           'superincomprehensibleness'])

# if __name__ == '__main__':
#     unittest.main()
