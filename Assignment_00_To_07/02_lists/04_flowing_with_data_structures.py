def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    message = input("\n\033[1;3mEnter a message to copy: \033[0m")
    my_list = []
    print("\nList before:", my_list)
    add_three_copies(my_list, message)
    print("\nList after:", my_list)

if __name__ == "__main__":
    main()
