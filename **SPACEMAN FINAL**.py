import random

# change the guess array NameError

# To DO:
# 1) Ensure user doesn't enter a value twice

letterCount = 0 

word_list = [
    "apple", "banana", "education", "house", "fridge", "game", "aaaaaaaab"
]
print("--------------------")
print("----SPACEMAN 2.0----")
print("--------------------")


def setUpGame():
    lives = 6
    word = word_list[random.randint(0, len(word_list)) - 1]
    previouslyGuessedLetters = []

    guess = []
    for i in range(0, len(word)):
        guess.append("_")

    return lives, word, guess, previouslyGuessedLetters

# CHANGE GUESS GUESS ARRAY TO A DIFFERENT NAME 

def Game():
  lives, word, guess, previouslyGuessedLetters = setUpGame() 
  run = True

  while (run==True and letterCount != len(word)):
      printArray(guess)
      playerGuess = getUserInput()
      isLetterInWord = checkLetter(word, playerGuess)

      if(playerGuess in previouslyGuessedLetters):
        print("You have already guessed this letter")
      else:
        if(isLetterInWord):
            guess = updateGuess(word, playerGuess, guess)
        else:
            lives = lives - 1
            if(lives == 0):
              run = False
            else:
              print("\nYou guessd the letter wrong, you have {} lives remaining".format(lives))
        previouslyGuessedLetters.append(playerGuess)

  if(letterCount == len(word)):
    print("Well done, you have guessed the word correctly!")
  else:
    print("\nYou have ran out of lives, the word was {}".format(word))

def printArray(guess):
    for letter in guess:
        print(letter, end=" ")
    print('\n')

def getUserInput():
    playerGuess = input("Please enter a letter: ")
    return playerGuess


def checkLetter(word, letter):
    if letter in word:
        return True
    else:
        return False

def updateGuess(word, userGuess, guess):
    count = 0
    for letter in word:
        if letter == userGuess:
            guess[count] = letter
            global letterCount
            letterCount = letterCount + 1
        count = count + 1
    return guess


Game()
