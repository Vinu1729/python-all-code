num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


if num > 0:
    print("The number is Positive.")
    if num > 100:
        print("The number is greater than 100.")
    else:
        print("The number is less than or equal to 100.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")