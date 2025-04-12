import random

NUM_SIDES = 6

def roll_dice():
   
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total: {total}")
    print("-------------------") 

def main():
    
    my_number = 10
    
    print(f"My number in main() is: {my_number}")
    
    print('\nDice Simulator!')
    
    print("\nLet's roll the dice three times!")
   
    for i in range(3):
        
        print(f"\nRoll #{i+1}:")
        roll_dice()
    
    print(f"\nAfter all rolls, my number in main() is still: {my_number}")

if __name__ == '__main__':
    main()
    
    
    
    
    