
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def get_list_of_ints():
    lst = []
    user_input = input("\033[34mEnter an integer or press enter to stop: \033[0m")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("\033[34mEnter an integer or press enter to stop: \033[0m")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()