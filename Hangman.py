# Writen by Steven Ngwenya
# Hangman
import random


def random_arrange(word):  # this function returns letters of the word randomly arranged

    rand_nums = []
    mixed_letters = ""
    i = 0
    while i < len(word):  # Compute random numbers len(word) times
        rand_num = random.randint(0, len(word) - 1)
        if rand_num in rand_nums:  # This means the number has already been computed before
            continue               # Therefore programme gets another random number

        else:
            mixed_letters += word[rand_num]
            rand_nums.append(rand_num)
            i += 1
    return mixed_letters


play_again = True
while play_again:
    # progress = ""  # As for user's progress
    lives = 10  # The user gets 10 chances to guess the letters of the word
    print("\n" * 2)

    #  A list of random words
    # The input function prompts the user's name and add it to the random words list
    random_word = ["grace", "television", "iphone", "ipad", "children", "snake", "hangman", "phone", "donkey", "horse",
                   "durban", "london", "amanda", "brian", "team", "pie", "pizza", "month", "sing", "gospel", "cinema",
                   "ice", "water", "taste", "red", "animals", "book", "pink", "house", "medal", "joke", "rugby",
                   "scared", "zebra", "run", "medal", "nokia", "god", "drink", "school", "ball", "aeroplane", "toyota",
                   "ruler", "paint", "sun", "apple", "tooth", "female", "chocolate", "banana", "food", "soccer",
                   "trouble", "hangman", "keyboard", "laptop", "computer", "netflix", "facebook", "tiktok", "twitter",
                   "lazy", "money", "king", "yellow", "milk", "america", "china", "dog", "cow", "pencil", "gym",
                   "music", "instagram", "spotify", "news", "english", "perfect", "keyboard", "school", "bus"
                   "work", "holiday", "peanuts", "work", "party", input("welcome!, enter your name: ")]

    print("Hi", random_word[-1], input("press enter to continue: "))  # Greet the user
    print("\n" * 3)

    random_number = random.randint(1, len(random_word))  # The random number must be not > the length of list

    guess = random_word[random_number - 1]  # this is the random word that the user has to guess
    # guess="Shingy"  # For testing purposes
    guess = guess.lower()
    guess = list(guess)  # This word has to be a list of letters

    # initially the user has an empty progress
    # example. if the random word is apple then progress = _____ since apple has 5 letters
    # if the user guesses any correct letter of the word apple example "p"
    # the second "_" is replaced with p leaving progress = _p___
    # Therefore progress has to be a list of dashes

    progress = "_" * len(guess)
    progress = list(progress)

    # this is the random word that the user has to guess but it remains unchanged for later usage
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

    play = True
    if play:
        while lives >= 0:

            letter = input("Enter 1 To get the hint or guess the letter: ")
            if letter == "1":  # The user only gets one chance to guess the whole word not letters
                if lives > 3 and len(guess) > 4:  # the user has to have at least 3 lives remaining and the word has
                    # to have at least 5 letters otherwise the user has to choose another type of hint.

                    hint = random_arrange(guess1)
                    print("Write the full word with the letters below\n" + hint)
                    full_word = (input("Enter the word: ")).lower()

                    if full_word == guess1:
                        print("Congratulations YOU WON!")
                        play = False
                        break

                    else:  # If the user guesses the wrong word then its a game over
                        print("GAME OVER, the correct word is: ", guess1)
                        play = False
                        break

                else:
                    print("OOPS, You don't qualify to choose this hint!")

            elif letter.lower() in guess:
                print("\n" * 2)
                print("This letter is on position", guess.index(letter) + 1)
                progress[guess.index(letter)] = letter  # Already explained how progress works above, line 34
                finish.append('#')  # already explained this , line 45
                print(progress)  # always show the his/her progress after every guess
                guess[guess.index(letter)] = "#"  # already explained this part
                # print("\n" * 2)

                if guess == finish:
                    print("Congratulations YOU WON!")

                    break

            else:  # if the user guesses a wrong letter
                lives -= 1
                print("\n" * 2)
                print(letter, "is not part of the word")
                print(progress)
                if lives >= 0:
                    print("you have", lives, "lives remaining")
                # print("\n")

    if lives < 0:
        print("GAME OVER, the correct word is: ", guess1)
        play = False

    if (play is False) or (guess == finish):
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.lower() == "y":
            play_again = True

        else:
            play_again = False
