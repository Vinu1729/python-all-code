def pattern_a():
    for i in range(1, 5):
        print("*" * i)

def pattern_b():
    for i in range(1, 6, 2):
        print(" " * ((5 - i) // 2) + "*" * i)
    for i in range(3, 0, -2):
        print(" " * ((5 - i) // 2) + "*" * i)

def pattern_c():
    rows = [7, 5, 3, 1]
    for r in rows:
        print(" " * ((7 - r) // 2) + "".join(["1" if i % 2 == 0 else "0" for i in range(r)]))

def even_numbers():
    num = 2
    while num <= 100:
        print(num, end=" ")
        num += 2
    print()

def sum_natural_numbers():
    print(f"Sum of first 10 natural numbers: {sum(range(1, 11))}")

def fibonacci_series():
    n = int(input("Enter the number of terms: "))
    a, b = 0, 1
    print("Fibonacci Series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} is {fact}")

def reverse_number():
    num = input("Enter a number: ")
    print(f"Reversed number: {num[::-1]}")

def sum_of_digits():
    num = input("Enter a number: ")
    total = sum(int(digit) for digit in num)
    print(f"Sum of digits: {total}")

def check_palindrome():
    num = input("Enter a number: ")
    if num == num[::-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Print Pattern A")
        print("2. Print Pattern B")
        print("3. Print Pattern C")
        print("4. Print Even Numbers from 1 to 100")
        print("5. Find Sum of First 10 Natural Numbers")
        print("6. Print Fibonacci Series")
        print("7. Calculate Factorial")
        print("8. Reverse a Number")
        print("9. Sum of Digits in a Number")
        print("10. Check if a Number is a Palindrome")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            pattern_a()
        elif choice == '2':
            pattern_b()
        elif choice == '3':
            pattern_c()
        elif choice == '4':
            even_numbers()
        elif choice == '5':
            sum_natural_numbers()
        elif choice == '6':
            fibonacci_series()
        elif choice == '7':
            factorial()
        elif choice == '8':
            reverse_number()
        elif choice == '9':
            sum_of_digits()
        elif choice == '10':
            check_palindrome()
        elif choice == '11':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()