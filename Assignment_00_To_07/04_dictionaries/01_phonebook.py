def READ_PHONE_NUMBERS():
    phone_book = {}
    
    while True:
        name = input("Enter Contact Name : ")
        if name == "":
            break
        phone_number = input("Enter Contact's Phone Number : ")
        phone_book[name] = phone_number
    return phone_book

def PRINT_PHONE_BOOK(phone_book):
    for name in phone_book:
        print(f"{name} : {phone_book[name]}")
        
def LOOKUP_NUMBER(phone_book):
    while True:
        name = input("Enter Contact's Name To Lookup: ")
        if name == "":
           break
        if name not in phone_book:
           print(f"{name} is not in Contact List.")
        else:
           print(f"{name}'s Phone Number is {phone_book[name]}.")

def main():
    phone_book = READ_PHONE_NUMBERS()
    PRINT_PHONE_BOOK(phone_book)
    LOOKUP_NUMBER(phone_book)



if __name__ == '__main__':
    main()