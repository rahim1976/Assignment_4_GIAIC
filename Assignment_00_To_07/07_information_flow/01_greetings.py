def main():
    name = input("\033[1;3mWhat's your name? \033[0m")
    print(greet(name))


def greet(name):
    return (f"Greetings {name}👋")
	
if __name__ == '__main__':
    main()
