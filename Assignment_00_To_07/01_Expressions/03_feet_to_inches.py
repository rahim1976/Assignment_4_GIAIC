def main():
   
   feet: float = float(input('\033[1m\033[3mEnter Your Number in Feet: \033[0m'))
   
   inches = feet * 12   
   
   print(f'{feet} Feet is {inches} Inches')   
   
if __name__ == '__main__':
    main()