try:
    int(input("Enter a number"))
except ValueError:
    print("Invalid input")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero")