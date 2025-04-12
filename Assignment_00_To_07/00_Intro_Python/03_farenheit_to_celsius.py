def main():
    print('\nFahrenheit To Celsius')
    
    fahrenheit = float(input("\n\033[1;3mEnter Temprature in Fahrenheit: \033[0m"))
    
    celsius = (fahrenheit - 32) * 5/9
    
    print(f"\nTemprature: {fahrenheit}°F = {celsius:.2f}°C")
    
if __name__ == "__main__":
    main()