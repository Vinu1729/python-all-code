import math

def usd_to_inr():
    usd = float(input("Enter amount in USD: "))
    exchange_rate = 83.0  # Update exchange rate as needed
    inr = usd * exchange_rate
    print(f"{usd} USD is equal to {inr} INR")

def convert_bits():
    bits = int(input("Enter the number of bits: "))
    MB = bits / (8 * 1024 * 1024)
    GB = MB / 1024
    TB = GB / 1024
    print(f"{bits} bits = {MB:.6f} MB = {GB:.6f} GB = {TB:.6f} TB")

def find_square_root():
    num = float(input("Enter a number: "))
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt}")

def rectangle_area():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Area of rectangle: {area}")

def square_properties():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"Area: {area}, Perimeter: {perimeter}")

def cylinder_properties():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = math.pi * radius ** 2 * height
    surface_area = 2 * math.pi * radius * (radius + height)
    print(f"Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")

def swap_values():
    a = input("Enter first value: ")
    b = input("Enter second value: ")
    a, b = b, a  # Swapping
    print(f"After swapping: a = {a}, b = {b}")

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Convert USD to INR")
        print("2. Convert Bits to MB, GB, TB")
        print("3. Find Square Root")
        print("4. Find Area of Rectangle")
        print("5. Calculate Area and Perimeter of Square")
        print("6. Calculate Surface Area and Volume of Cylinder")
        print("7. Swap Two Variables")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            usd_to_inr()
        elif choice == '2':
            convert_bits()
        elif choice == '3':
            find_square_root()
        elif choice == '4':
            rectangle_area()
        elif choice == '5':
            square_properties()
        elif choice == '6':
            cylinder_properties()
        elif choice == '7':
            swap_values()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()