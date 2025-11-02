# Robert Rowlands
# CIS256 Fall 2025
# EX 4

# Word guessing game



#import libraries
import random


# create simple list of words
word_list = ["GHOSTS", "GOBLINS", "VAMPIRES", "WEREWOLVES", "ZOMBIES", "FAIRIES"]

# function to hide the word and reveal letters
def hide_word(the_word, guessed_letters):
    hidden = ""
    for ch in the_word:
        if ch in guessed_letters:
            hidden += ch
        else:
            hidden += "_"
    return hidden

#test function
print (hide_word("TestingWords", {"r", "S", "T", "L", "n","E"}))
