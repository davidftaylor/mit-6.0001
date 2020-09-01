# Problem Set 2, hangman.py
# Name: David Taylor
# Time spent: 2 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    matches = 0
    for letter in secret_word:
        if letter in letters_guessed:
            matches += 1
    if matches == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_list = list(secret_word)
    for index in range(len(secret_word)):
        if secret_word[index] not in letters_guessed:
            secret_list[index] = ' _ '
    word_so_far = ''.join(secret_list)
    return(word_so_far)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters_list = list(string.ascii_lowercase)
    for letter in letters_guessed:
        if letter in all_letters_list:
            all_letters_list.remove(letter)
    remaining_letters = ''.join(all_letters_list)
    return remaining_letters

guesses = 6
num_warnings = 3

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global guesses
    global num_warnings
    
    def warnings():
        global guesses
        global num_warnings
        if num_warnings == 0:
            print('You have been penalized a guess.')
            guesses -= 1
        else:
            num_warnings -= 1
            if num_warnings == 0 or num_warnings >= 2:
                print('You must enter a single letter and it must not have been\
 guessed before.', num_warnings, 'warnings remaining. You will start\
 losing guesses if you accrue 3 warnings.')
            elif num_warnings == 1:
                print('You must enter a single letter and it must not have been\
 guessed before.', num_warnings, 'warning remaining. You will start\
 losing guesses if you accrue 3 warnings.')
                  
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    letters_guessed = []
    print('You have', num_warnings, 'warnings left.')
    while guesses > 0:
        print('You have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input('Guess a letter: ')
        if guess in string.ascii_lowercase or guess in string.ascii_uppercase:
            if guess in letters_guessed:
                warnings()
                continue
            if guess in string.ascii_uppercase:
                guess = guess.lower()
            if len(guess) != 1:
                warnings()
                continue
            letters_guessed.append(guess)
            word_so_far = get_guessed_word(secret_word, letters_guessed)
            if guess in secret_word:
                print('Good guess:', word_so_far)
                if is_word_guessed(secret_word, letters_guessed):
                    print('------------')
                    print('Congratulations! You win.')
                    print('Your total score for this game is:', guesses*len(secret_word))
                    break
            else:
                print('Oops! That letter is not in my word:', word_so_far)
                if guess in 'aeiou':
                    guesses -= 2
                else:
                    guesses -= 1
        else:
            warnings()
            continue
        print('------------')
    
    if not is_word_guessed(secret_word, letters_guessed):
        print('Sorry! You stink! The word was', secret_word)
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
        for index in range(len(my_word)):
            if my_word[index] in string.ascii_lowercase:
                if my_word[index] != other_word[index]:
                    return False
                    break
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    my_word = my_word.replace(' ', '')
    for word in load_words():
        if match_with_gaps(my_word, word):
            matches.append(word)
            for letter in my_word:
                if letter in string.ascii_lowercase:
                    if my_word.count(letter) != word.count(letter):
                        if word in matches:
                            matches.remove(word)
    if matches == '':
        print('No matches found.')
    else:
        print('Possible word matches are:', ' '.join(matches))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global guesses
    global num_warnings
    
    def warnings():
        global guesses
        global num_warnings
        if num_warnings == 0:
            print('You have been penalized a guess.')
            guesses -= 1
        else:
            num_warnings -= 1
            if num_warnings == 0 or num_warnings >= 2:
                print('You must enter a single letter and it must not have been\
 guessed before.', num_warnings, 'warnings remaining. You will start\
 losing guesses if you accrue 3 warnings.')
            elif num_warnings == 1:
                print('You must enter a single letter and it must not have been\
 guessed before.', num_warnings, 'warning remaining. You will start\
 losing guesses if you accrue 3 warnings.')
                  
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('Enter * at any point for a list of possible matches.')
    letters_guessed = []
    print('You have', num_warnings, 'warnings left.')
    while guesses > 0:
        print('You have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        guess = input('Guess a letter: ')
        if guess in string.ascii_lowercase or guess in string.ascii_uppercase:
            if guess in letters_guessed:
                warnings()
                continue
            if guess in string.ascii_uppercase:
                guess = guess.lower()
            if len(guess) != 1:
                warnings()
                continue
            letters_guessed.append(guess)
            word_so_far = get_guessed_word(secret_word, letters_guessed)
            if guess in secret_word:
                print('Good guess:', word_so_far)
                if is_word_guessed(secret_word, letters_guessed):
                    print('------------')
                    print('Congratulations! You win.')
                    print('Your total score for this game is:', guesses*len(secret_word))
                    break
            else:
                print('Oops! That letter is not in my word:', word_so_far)
                if guess in 'aeiou':
                    guesses -= 2
                else:
                    guesses -= 1
        else:
            if guess == '*':
                show_possible_matches(word_so_far)
            else:
                warnings()
                continue
        print('------------')
    
    if not is_word_guessed(secret_word, letters_guessed):
        print('Sorry! You stink! The word was', secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
