import re
from nltk.corpus import words

# Removes all punctuation except apostrophes
regex = re.compile('[%s]' % re.escape('!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~')) 

# Dictionary of English words
english_words = words.words()
    
# Calculate percentage of the text that has english words
def eng_pct(words):
    if words == []:
        return 0 # no words => none is english
    
    eng_count = 0
    for word in words:
        if word in english_words:
            eng_count += 1
    return eng_count / len(words)

# Determine if the message is english based on percentage of english words 
# and percentage of characters that are letters   
def check(text, min_word_pct=0.6, min_letter_pct=0.85):
    
    # Clean the text - remove punctuation and make everything lower case
    clean_text = regex.sub('',text.lower())
    
    # Find letter percentage
    num_letters = len(clean_text)
    letter_pct = num_letters/len(text)
    
    # Find word percentage
    words = clean_text.split()
    word_pct = eng_pct(words)
    
    print(word_pct, letter_pct)
    return ((letter_pct >= min_letter_pct) and (word_pct >= min_word_pct))
