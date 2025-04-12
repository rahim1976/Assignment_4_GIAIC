def main():
    print('\nTriangle Perimeter Calculator')
    
    length1 = float(input("\n\033[1;3mEnter Right Length: \033[0m"))
    length2 = float(input("\n\033[1;3mEnter Left Length: \033[0m"))
    length3 = float(input("\n\033[1;3mEnter Bottom Length: \033[0m"))
    
    perimeter = length1 + length2 + length3
    
    print(f"\nPerimeter of Triangle: {perimeter:.2f}")
    
if __name__ == "__main__":
    main()