def sum_list():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    print(f"Sum of all items: {sum(lst)}")

def multiply_list():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    result = 1
    for num in lst:
        result *= num
    print(f"Product of all items: {result}")

def largest_in_list():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    print(f"Largest number in the list: {max(lst)}")

def smallest_in_list():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    print(f"Smallest number in the list: {min(lst)}")

def reverse_list():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    print(f"Reversed list: {lst[::-1]}")

def common_items():
    list1 = list(map(int, input("Enter first list numbers separated by space: ").split()))
    list2 = list(map(int, input("Enter second list numbers separated by space: ").split()))
    common = list(set(list1) & set(list2))
    print(f"Common items: {common}")

def even_items():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    even_numbers = [num for num in lst if num % 2 == 0]
    print(f"Even numbers in the list: {even_numbers}")

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Sum all items in a list")
        print("2. Multiply all items in a list")
        print("3. Find the largest number in a list")
        print("4. Find the smallest number in a list")
        print("5. Reverse a list")
        print("6. Find common items in two lists")
        print("7. Select even items from a list")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            sum_list()
        elif choice == '2':
            multiply_list()
        elif choice == '3':
            largest_in_list()
        elif choice == '4':
            smallest_in_list()
        elif choice == '5':
            reverse_list()
        elif choice == '6':
            common_items()
        elif choice == '7':
            even_items()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()