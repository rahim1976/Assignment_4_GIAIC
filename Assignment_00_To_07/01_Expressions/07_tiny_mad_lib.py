SECTENCE_START = "Look At How The "

def main():
        ADJECTIVE = input("\033[1m\033[3mPlease Enter An Adjective: \033[0m")
        NOUN = input("\033[1m\033[3mPlease Enter A Noun: \033[0m")
        VERB = input("\033[1m\033[3mPlease Enter A Verb: \033[0m")

        
        FINAL_SENTENCE = (SECTENCE_START + ADJECTIVE + " " + NOUN + " " + VERB + ".")
        
        print(FINAL_SENTENCE)

if __name__ == '__main__':
    main()