def main():
    curr_value = int(input("Enter a number: "))
    print(curr_value, end=' ')
    
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ') # end=' ' means print on the same line

if __name__ == '__main__':
    main()