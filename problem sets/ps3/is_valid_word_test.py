from ps3 import *

def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure=False
    # test 1
    word = "hello"
    handOrig = get_frequency_dict(word)
    handCopy = handOrig.copy()

    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", handOrig)

        failure = True

    # Test a second time to see if word_list or hand has been modified
    if not is_valid_word(word, handCopy, word_list):
        print("FAILURE: test_is_valid_word()")

        if handCopy != handOrig:
            print("\tTesting word", word, "for a second time - be sure you're not modifying hand.")
            print("\tAt this point, hand ought to be", handOrig, "but it is", handCopy)

        else:
            print("\tTesting word", word, "for a second time - have you modified word_list?")
            wordInWL = word in word_list
            print("The word", word, "should be in word_list - is it?", wordInWL)

        print("\tExpected True, but got False for word: '" + word + "' and hand:", handCopy)

        failure = True


    # test 2
    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "Rapture"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True        

    # test 3
    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '"+ word +"' and hand:", hand)

        failure = True                        

    # test 4
    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        
        failure = True

    # test 5
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "EVIL"
    
    if  not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)
        
        failure = True
        
    # test 6
    word = "Even"

    if  is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print("\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)")        
        
        failure = True        

    if not failure:
        print("SUCCESS: test_is_valid_word()")
        
print("Testing is_valid_word...")
test_is_valid_word(word_list)