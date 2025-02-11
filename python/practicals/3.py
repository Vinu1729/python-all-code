a = 10
b = 3

floor_div = a // b

power = a ** b
remainder = a % b  # 10 % 3 = 1
print("Floor Division (10 // 3):", floor_div)
print("Exponentiation (10 ** 3):", power)
print("Modulus (10 % 3):", remainder)

#2
a = 10
b = 20
max_num = a if a > b else b

print("Maximum number is:", max_num)

#3
x = 10
y = 20

result = (x > 5) and (y > 15)

print("Result of AND:", result)

result1 = (x > 15) or (y > 15)

print("Result of OR:", result1)

result3 = not (x > 5)

print("Result of NOT:", result3)
#4

result4 = a + b
print("Addition:", result4)
result5 = a - b
print("Subtraction:", result5)
result6 = a * b
print("Multiplication:", result6)
result7 = a / b
print("Division:", result7)

and_result = a & b
or_result = a | b
not_result = ~a
print("Bitwise AND :", and_result)
print("Bitwise OR :", or_result)
print("Bitwise NOT ", not_result)