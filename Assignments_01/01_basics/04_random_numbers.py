import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for i in range(N_NUMBERS):
        random_num = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_num, end=" ") # end=" " means don't print a newline
    
    print()

if __name__ == '__main__':
    main()