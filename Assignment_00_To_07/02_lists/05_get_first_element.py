# Function 1 (Getting the first element of the list)
def get_first_element(lst):
    print(lst[0])

# Function 2 (Getting the list)
def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

# Function 3 (Returning the first element of the list)
def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()

