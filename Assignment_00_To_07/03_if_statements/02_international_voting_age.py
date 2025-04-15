PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE  = 48

def main():
    VOTER_AGE = int(input("\033[34mWhat's Your Age?: \033[0m"))
    
    if VOTER_AGE >= PETURKSBOUIPO_AGE:
        print(f"You Can Vote In Peturksbouipo because the voting age thier is {PETURKSBOUIPO_AGE}!")
    else:
        print(f"You Can't Vote In Peturksbouipo because the voting age thier is {PETURKSBOUIPO_AGE}!")
    
    if VOTER_AGE >= STANLAU_AGE:
        print(f"You Can Vote In stanlau because the voting age thier is {STANLAU_AGE}!")
    else:
        print(f"You Can't Vote In stanlau because the voting age thier is {STANLAU_AGE}!")
        
    if VOTER_AGE >= MAYENGUA_AGE:
        print(f"You Can Vote In mayengua because the voting age thier is {MAYENGUA_AGE}!")
    else:
        print(f"You Can't Vote In mayengua because the voting age thier is {MAYENGUA_AGE}!")
    
    
if __name__ == '__main__':
    main()