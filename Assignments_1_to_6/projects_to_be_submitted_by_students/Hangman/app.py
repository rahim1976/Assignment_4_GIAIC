import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()  # Convert word to uppercase for consistency

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed
    
    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show current state
        print('\n' + '='*50)
        print('You have' , lives,'lives left and You have used these letters:', ' '.join(sorted(used_letters)))
        
        # Show current word with dashes
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('_')
        print('\nCurrent word:', ' '.join(word_list))
        print('='*50 + '\n')
        
        # Get user input
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1
                print('\nLetter is not in word')
                
                
        elif user_letter in used_letters:
            print('\nYou already guessed that letter. Please try again')
            
        else:
            print('\nInvalid character. Please try again')
    
    if lives == 0:
        print('\nYou Died, sorry. The Word was', word)    
    else:
        print('\nCongratulations! You guessed the word:' ,word, '!!')

# Start the game
hangman()