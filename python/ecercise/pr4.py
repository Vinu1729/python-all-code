def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

def absolute_value():
    num = float(input("Enter a number: "))
    print(f"Absolute value of {num} is {abs(num)}")

def largest_of_three():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    largest = max(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")

def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")

def check_number():
    num = float(input("Enter a number: "))
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

def calculate_grade():
    marks = []
    for i in range(5):
        marks.append(float(input(f"Enter marks for subject {i+1}: ")))

    avg = sum(marks) / 5

    if avg >= 90:
        grade = 'A+'
    elif avg >= 80:
        grade = 'A'
    elif avg >= 70:
        grade = 'B'
    elif avg >= 60:
        grade = 'C'
    elif avg >= 50:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Average Marks: {avg:.2f}, Grade: {grade}")

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Check Even or Odd")
        print("2. Find Absolute Value")
        print("3. Find Largest Among Three Numbers")
        print("4. Check if a Year is a Leap Year")
        print("5. Check if Number is Positive, Negative, or Zero")
        print("6. Calculate Grade from 5 Subjects")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            check_even_odd()
        elif choice == '2':
            absolute_value()
        elif choice == '3':
            largest_of_three()
        elif choice == '4':
            check_leap_year()
        elif choice == '5':
            check_number()
        elif choice == '6':
            calculate_grade()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()