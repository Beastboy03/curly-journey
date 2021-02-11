# Writen by Steven Ngwenya
# Hangman
import random


# progress = ""  # As for user's progress
lives = 10	 # The user gets 10 chances to guess the letters of the word
print("Hello World!")  # Lol! nvm that
print("\n" * 2)

#  A list of random words
# The input function prompts the user's name and add it to the random words list
random_word = ["grace", "television", "children", "snake", "hangman", "phone", "donkey", "horse", "durban", "london",
               "hangman", "goku", "water", "taste", "red", "animals", "book", "pink", "house", "medal", "joke", "rugby",
               "scared", "zebra", "run", "medal", "nokia", "god", "drink", "school", "ball", "aeroplane", "toyota",
               "ruler", "paint", "sun", "apple", "tooth", "female", "chocolate", "banana", "food", "soccer", "trouble",
               "lazy", "money", "king", "yellow", "milk", "america", "china", "dog", "cow", "pencil", "gym", "music",
               "work", "holiday", "peanuts", "work", "party", input("welcome!, enter your name: ")]

print("Hi", random_word[-1], input("press enter to continue: "))  # Greet the user
print("\n" * 3)

random_number = random.randint(1, len(random_word))  # The random number must be not > the length of list

guess = random_word[random_number - 1]  # this is the random word that the user has to guess
guess = list(guess)  # This word has to be a list of letters
# guess="shingy"  # For testing purposes

# initially the user has an empty progress
# example. if the random word is apple then progress = _____ since apple has 5 letters
# if the user guesses any correct letter of the word apple example "p"
# the second "_" is replaced with p leaving progress = _p___
# Therefore progress has to be a list of dashes

progress = "_" * len(guess)
progress = list(progress)

# this is the random word that the user has to guess but it remains unchanged for latter usage
guess1 = random_word[random_number - 1]

#  finish variable initially is an empty list
#  for every correct letter guessed a "#" is added to this list
#  and that letter is replaced with a "#" in the variable named guess
#  guess will be similar to finish once the user guesses all letters of the word

finish = ""
finish = list(finish)  # finish has to be a list since string is immutable

print(progress)
print("guess the", len(guess), "letters of the word")
# print("\n")
# hello world
play = True
if play:
    while lives >= 0:
        letter = input("guess the letter: ")
        print("\n" * 2)
        if letter in guess:
            print("This letter is on position", guess.index(letter) + 1)
            progress[guess.index(letter)] = letter  # Already explained how progress works above, line 34
            finish.append('#')  # already explained this , line 45
            # print("\n" * 2)
            print(progress)  # always show the his/her progress after every guess
            guess[guess.index(letter)] = "#"  # already explained this part
            # print("\n" * 2)

            if guess == finish:
                print("Congratulations YOU WON!")

                break

        else:  # if the user guesses a wrong letter
            lives -= 1
            # print("\n" * 2)
            print(letter, "is not part of the word")
            print(progress)
            if lives >= 0:
                print("you have", lives, "lives remaining")
            # print("\n")

if lives < 0:
    print("GAME OVER, the correct word is: ", guess1)
    play = False