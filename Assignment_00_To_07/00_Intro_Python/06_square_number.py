def main():
    print('\nNumber Square Calculator')
    
    number = float(input("\n\033[1;3mEnter Your Number: \033[0m"))
    
    square = number ** 2
    
    print(f"\nSquare Of Your {number} Is: {square:.2f}")
    
if __name__ == "__main__":
    main()