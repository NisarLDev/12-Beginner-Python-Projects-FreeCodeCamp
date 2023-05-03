import random
import string
from words import words

def get_valid_words(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
      word = random.choice(words)
      
    return word
  
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    # getting user input
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    
    elif user_letterin used_letters:
        print('You already used that character. Please try again.')
       
    else:
        print('Invalidcharacter. Please try again.')
