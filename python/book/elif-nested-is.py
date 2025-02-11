#elif

age = 20

if age < 18:
    print("Minor")
elif age == 18:
    print("Just an Adult")
else:
    print("Adult")

#nested if
num = 10

if num > 0:
    print("Positive Number")
    if num % 2 == 0:
        print("Even Number")
