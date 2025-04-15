import random

TOTAL_NUM : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for i in range(TOTAL_NUM):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number, end=' ') # end=' ' USED FOR PRINTING IN THE SAME LINE
    

if __name__ == '__main__':
    main()