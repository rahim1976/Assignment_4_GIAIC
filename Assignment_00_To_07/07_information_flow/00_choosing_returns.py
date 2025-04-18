ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("\033[34mHow old is this person?: \033[0m"))
    result = is_adult(age)
    print(f"Is this person an adult? {result}")

if __name__ == "__main__":
    main()