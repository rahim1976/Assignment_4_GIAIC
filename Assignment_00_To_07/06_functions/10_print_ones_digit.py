def print_ones_digit(num: int):
    ones_digit = num % 10
    print("The ones digit is", ones_digit)

def main():
    num = int(input("\033[34mEnter a number: \033[0m"))
    print_ones_digit(num)

if __name__ == '__main__':
    main()