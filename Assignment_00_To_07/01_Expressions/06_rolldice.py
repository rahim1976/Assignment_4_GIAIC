import random

TOTAL_DICE_SIDES = 6

def main():
    
    # random.seed(1) 
    # benificial in debugging
    
    
    # Roll die
    die1 = random.randint(1, TOTAL_DICE_SIDES)
    die2 = random.randint(1, TOTAL_DICE_SIDES)
    
    # Get their total
    total = die1 + die2
    
    # Print out the results
    print("Dice have", TOTAL_DICE_SIDES, "sides each.")
    print("First Die:", die1)
    print("Second Die:", die2)
    print("Total of Both dice:", total)


if __name__ == '__main__':
    main()
