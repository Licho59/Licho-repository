# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:13:58 2017

@author: Leszek
"""

import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar\
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk\
lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot\
pidgeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth\
snake spider stork swan tigger trout turkey turtle weasel whale wolf wombat\
zebra'.split()

def getRandomWord(wordList):
    #This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)): # replace blanks with correctly
    # guessedletters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks:#show the secret word with spaces between each letter
        print(letter, end=' ')
        print()
            
    
    
    
    
    
    
      