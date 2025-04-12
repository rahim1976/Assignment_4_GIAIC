def main():
    print("\nThis Program Adds Two Numbers")
    
    number1 = input('\nEnter first number: ')
    number1 = int(number1)    

    number2 = input('\nEnter second number: ')
    number2 = int(number2)
    
    total= number1 + number2
    
    print(f'\nYour Answer Is: {total}')    

if __name__ == '__main__':
    main()