def main():
    C = 299792458  # Speed of light in m/s
    mass_in_kg = float(input("\033[1m\033[3mEnter kilos of mass: \033[0m"))

    # Calculate energy using E=mc²
    energy_in_joules = mass_in_kg * (C ** 2)

    # Displaying results
    print("\n=== Energy Calculation ===")
    print(f"Mass (m) = {mass_in_kg} kg")
    print(f"Speed of light (c) = {C} m/s")
    print(f"\nEnergy (E) = {energy_in_joules} Joules")
    print("=== End of Calculation ===")

if __name__ == '__main__':
    main()
   
