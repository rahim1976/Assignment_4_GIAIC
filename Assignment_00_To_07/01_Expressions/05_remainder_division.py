def main():
    
    dividend = int(input("\033[1m\033[3mPlease Enter A Number To Be Divided: \033[0m"))
    divisor = int(input("\033[1m\033[3mPlease Enter A Number To Divide by: \033[0m"))
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Display results
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
