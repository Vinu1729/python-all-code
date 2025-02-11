numbers = [5, 2, 8, 2, 9, 2, 3]

numbers.sort()
print("Sorted List:", numbers)

count_of_2 = numbers.count(2)
print("Count of 2 in the list:", count_of_2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

list1.extend(list2)
print("List after using extend():", list1)

popped_item = numbers.pop()
print("Popped Item:", popped_item)
print("List after pop:", numbers)


popped_index_2 = numbers.pop(2)
print("Popped Item at index 2:", popped_index_2)
print("List after popping index 2:", numbers)