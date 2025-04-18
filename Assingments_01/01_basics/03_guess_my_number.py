import random

def main():
    random_number = random.randint(1,99)
    guess = 0
    while guess!= random_number:
        guess = int(input(f'Guess a number between 1 and 99: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:  
            print('Sorry, guess again. Too high')

    print(f'Yay, Congrats. You have guessed the number {random_number} correctly!')

    
if __name__ == '__main__':
    main()