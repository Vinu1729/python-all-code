def min_max_tuple():
    tpl = tuple(map(int, input("Enter numbers separated by space: ").split()))
    print(f"Minimum: {min(tpl)}, Maximum: {max(tpl)}")

def find_repeated_items():
    tpl = tuple(map(int, input("Enter numbers separated by space: ").split()))
    repeated_items = {item for item in tpl if tpl.count(item) > 1}
    print(f"Repeated items: {list(repeated_items)}" if repeated_items else "No repeated items found.")

def number_to_words():
    num_str = input("Enter a number: ")
    words_dict = {
        '0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four",
        '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"
    }
    words = " ".join(words_dict[digit] for digit in num_str if digit in words_dict)
    print(f"Number in words: {words}")

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Find Minimum and Maximum from a Tuple")
        print("2. Find Repeated Items in a Tuple")
        print("3. Convert Number to Words")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            min_max_tuple()
        elif choice == '2':
            find_repeated_items()
        elif choice == '3':
            number_to_words()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()