import math 

def main():
    
    AB: float = float(input('Enter The Length Of AB: '))
    AC: float = float(input('Enter The Length Of AC: '))
    
    BC: float = math.sqrt(AB**2 + AC**2)
    
    print("The Length of BC (the hypotnenuse) is: " + str(BC))
    
if __name__ == '__main__':
    main()