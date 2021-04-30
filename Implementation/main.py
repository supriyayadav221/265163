import random
import string
from Implementation.src.wordsFile import words
from Implementation.src.hangmanVisual import chancesVisualDictionary
# Hangman game of words, to guess letters in 7 chances


def getValidWord(words):
    word = random.choice(words)   # randomly chooses any word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangmanGame():
    valid_word = getValidWord(words)
    wordLetters = set(valid_word)
    alphabetSet = set(string.ascii_uppercase)
    guessedLetters = set()

    chances = 7

    while len(wordLetters) > 0 and chances > 0:
        print(chances, "chances left and you have already guessed these letters ", " ".join(guessedLetters))

        listOfWord = [character if character in guessedLetters else '_' for character in valid_word]
        print(chancesVisualDictionary[chances])
        print("Current word is: ", " ".join(listOfWord))

        userInputLetter = input("Guess a letter: ").upper()
        if userInputLetter in alphabetSet - guessedLetters:
            guessedLetters.add(userInputLetter)
            if userInputLetter in wordLetters:
                wordLetters.remove(userInputLetter)
                print('')
            else:
                chances -= 1
                print("\n Your inputted letter, ", userInputLetter, " is not a word")
        elif userInputLetter in guessedLetters:
            print('\nYou have already guessed that letter, please guess another')

        else:
            print("\n Not a valid letter")

    if chances == 0:
        print(chancesVisualDictionary[chances])
        print("Sorry, you lost. Correct word was ", valid_word)
    else:
        print("Hurray ! You won the game. The w0rd was ", valid_word, "!")


if __name__ == '__main__':
    hangmanGame()
