def get_user_numbers():
    numbers = []
    while True:
        user_input = input("\033[34mEnter a number: \033[0m")
        
        if user_input == '': 
            break
        else:
            num = int(user_input)
            numbers.append(num)  
    return numbers

def count_numbers(num_lst):
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1  
        else:
            num_dict[num] = 1  
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
    numbers = get_user_numbers()
    num_dict = count_numbers(numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()