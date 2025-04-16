def main():
    FRUITS = {'Apple': 10, 'Banana': 5, 'Orange': 8, 'Mango': 12, 'Kiwi': 7}
    
    TOTAL_COST = 0
    for FRUIT_NAME in FRUITS:
        price = FRUITS[FRUIT_NAME]
        AMMOUNT_OF_FRUITS = int(input(f"\033[34mHow many {FRUIT_NAME}s do you want to buy?: \033[0m"))
        TOTAL_COST += price * AMMOUNT_OF_FRUITS
        
    print(f"Total cost: ${TOTAL_COST}")
    
    

if __name__ == '__main__':
    main()