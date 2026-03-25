#Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))
operation = input("Operation: ").strip().lower()

if operation == "add":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
elif operation == "multiply":
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
elif operation == "subtract":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
else:
    print()