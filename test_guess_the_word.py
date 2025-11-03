# Robert Rowlands
# CIS256 Fall 2025
# EX 4_1

# Testing using pytest


# importing things to test
from guess_the_word import word_list, word_rand, hide_word

# test if word is from list
def test_the_word():

    # Test 1 is word in word list
    for i in range(20):
        chosen_word = word_rand(word_list)
        assert chosen_word in word_list


    # Test 2 do the guesses work right
def test_the_guess():
    the_word = "ZOMBIES"

    hidden_word = hide_word(the_word, {"Z", "O"})
    assert hidden_word == "ZO_____"

    hidden_word = hide_word(the_word, {"Z", "Y"})
    assert hidden_word == "Z______"

    hidden_word = hide_word(the_word, {"A", "C"})
    assert hidden_word == "_______"
    

    





    
