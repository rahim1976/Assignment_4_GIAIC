def main():
    lst = []  # Empty list

    val = input("Enter a value: ")  # First value
    while val:  # While the user input isn't an empty value
        lst.append(val) 
        val = input("Enter a value: ")  # For upcoming values

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()