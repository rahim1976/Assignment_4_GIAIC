def main():
    numbers: list[int] = [5, 10, 15, 20, 25]
    
    for i in range(len(numbers)):
        NUMBER_IN_INDEX = numbers[i]
        numbers[i] = NUMBER_IN_INDEX * 2
    
    print(numbers)
 
if __name__ == '__main__':
    main()