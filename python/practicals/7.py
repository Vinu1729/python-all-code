empty_tuple = ()
empty_tuple_alt = tuple()  # 2
print("Empty Tuple:", empty_tuple)

existing_tuple = (10, 20, 30, 40, 50)


new_tuple = (existing_tuple[1], existing_tuple[3])

print("Existing Tuple:", existing_tuple)
print("New Tuple with selected elements:", new_tuple)