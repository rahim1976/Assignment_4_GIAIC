def main():
    lst = []  # Empty list

    val = input("\033[34mEnter a value: \033[0m")  # First value 
    while val:  # While the user input isn't an empty value
        lst.append(val) 
        val = input("\033[34mEnter a value: \033[0m")  # For upcoming values 

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()