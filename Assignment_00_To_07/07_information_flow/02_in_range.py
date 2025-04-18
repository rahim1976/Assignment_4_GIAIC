def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    n = int(input("\033[1;3mEnter a number to check: \033[0m"))
    low = int(input("\033[1;3mEnter the lower bound: \033[0m"))
    high = int(input("\033[1;3mEnter the higher bound: \033[0m"))
    result = in_range(n, low, high)
    print(f"Is {n} between {low} and {high}? {result}")

if __name__ == '__main__':
    main()