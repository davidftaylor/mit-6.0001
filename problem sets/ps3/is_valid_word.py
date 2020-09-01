def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    if word in word_list:
        for letter in word:
            if word.count(letter) > hand[letter]:
                return False
        return True
    return False
    
print(is_valid_word('hello', {'h': 1, 'e': 1, 'l': 2, 'o': 1}, ['hello']))
