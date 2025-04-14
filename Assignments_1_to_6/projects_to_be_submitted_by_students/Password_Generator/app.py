import random

print('Wellcome To This Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$%&*.'

number = input("Write Ammount Of Passwords You Want To Generate: ")
number = int(number)

length = input("Write The Password Length You Want To Generate: ")
length = int(length)

print("\nCopy Your Passwords Below: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)