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

# Main Game

def the_game():

    # get the word
    the_word = word_rand(word_list)
    
    # set the guessed letters
    guessed_letters = set()

    # number of wrong answers before losing
    chances = 7

    # Game Opening
    print("!!!!!The Word Guessing Game!!!!!\n")
    print("Guess a single letter at time.\nIf you guess correct, the letter will be shown.\nIf you guess incorrectly, you will lose a chance.\n")
    print(f"You have {chances} to guess the word.\n")
    print(f"Guess this word: {hide_word(the_word, guessed_letters)}\n")

    # actual game
    # check for chances
    while chances > 0 and not word_complete(the_word, guessed_letters):
        
        #get user input
        user_guess = input("Enter a letter: ").upper().strip()
        
        # validate user input
        
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single letter between A and Z.")
            continue

        if user_guess in guessed_letters:
            print(f"You already guessed the letter: {user_guess}.\nTry Again.")
            continue

        # add the letter to the set if valid.
        guessed_letters.add(user_guess)

        if user_guess in the_word:
            print(f"You guessed a correct letter! {user_guess} is in the word.\n")

        # remove a chance if it is not.
        else:
            chances += -1
            print(f"Sorry, {user_guess} is not in the word.\nYou have {chances} remaining.\n")

        # show the word and the guessed letters so far
        print(f"Guess this word: {hide_word(the_word, guessed_letters)}\n")
        print(f"Letters guessed so far: {' '.join(sorted(guessed_letters))}\n")

    # Win or lose game
    if word_complete(the_word, guessed_letters):
        print(f"You won the game!\nThe word was: {the_word}.\n")

    else:
        print(f"Sorry, you ran out of chances.\nThe word was: {the_word}.")


# run the thing
if __name__ == "__main__":
    the_game()
    # keep window open
    input("\nPress Enter to exit...")
        
            

            
    
    

    
    
    
    
