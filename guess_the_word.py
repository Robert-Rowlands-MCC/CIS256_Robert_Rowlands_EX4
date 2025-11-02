# Robert Rowlands
# CIS256 Fall 2025
# EX 4

# Word guessing game



#import libraries
import random

# create simple list of words
word_list = ["GHOSTS", "GOBLINS", "VAMPIRES", "WEREWOLVES", "ZOMBIES", "FAIRIES"]

# 


# Functions

# function to choose a random word
def word_rand(word_list):
    return random.choice(word_list)


# function to hide the word and reveal letters
def hide_word(the_word, guessed_letters):
    hidden = ""
    for ch in the_word:
        if ch in guessed_letters:
            hidden += ch
        else:
            hidden += "_"
    return hidden


# function to see if all the letters have been guessed
def word_complete(the_word, guessed_letters):
    for ch in the_word:
        if ch not in guessed_letters:
            return False
    return True

# testing

guessed_letters = ["G", "H", "O", "S", "T"]
the_word = "GHOSTS"

print(hide_word(the_word, guessed_letters))
print(word_complete(the_word, guessed_letters))

guessed_letters = ["G", "H", "O", "S", "r"]
print(hide_word(the_word, guessed_letters))
print(word_complete(the_word, guessed_letters))
