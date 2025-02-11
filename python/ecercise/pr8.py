def create_add_remove_set():
    my_set = set(map(int, input("Enter elements separated by space: ").split()))
    print(f"Initial Set: {my_set}")

    new_elements = set(map(int, input("Enter new elements to add (separated by space): ").split()))
    my_set.update(new_elements)
    print(f"Set after adding elements: {my_set}")

    remove_element = int(input("Enter an element to remove: "))
    if remove_element in my_set:
        my_set.remove(remove_element)
        print(f"Set after removing {remove_element}: {my_set}")
    else:
        print(f"{remove_element} not found in the set.")

def set_operations():
    set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))
    set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Set Difference (Set1 - Set2): {set1 - set2}")
    print(f"Symmetric Difference: {set1 ^ set2}")

    clear_choice = input("Do you want to clear the first set? (yes/no): ").strip().lower()
    if clear_choice == "yes":
        set1.clear()
        print("First set cleared.")

def min_max_set():
    my_set = set(map(int, input("Enter elements separated by space: ").split()))
    print(f"Minimum: {min(my_set)}, Maximum: {max(my_set)}")

def length_of_set():
    my_set = set(map(int, input("Enter elements separated by space: ").split()))
    print(f"Length of the set: {len(my_set)}")

def main():
    while True:
        print("\nSelect an operation:")
        print("1. Create a set, add members, and remove an item")
        print("2. Perform set operations (union, intersection, difference, symmetric difference, clear)")
        print("3. Find Minimum and Maximum in a Set")
        print("4. Find Length of a Set")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_add_remove_set()
        elif choice == '2':
            set_operations()
        elif choice == '3':
            min_max_set()
        elif choice == '4':
            length_of_set()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()