# Robert Rowlands
# CIS256 Fall 2025
# EX 4_1

# Testing using pytest

from guess_the_word import word_list, word_rand

# test if word is from list
def test_guess_the_word():
    for i in range(20):
        chosen_word = word_rand(word_list)
        assert chosen_word in word_list



    
