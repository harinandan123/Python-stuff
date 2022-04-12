# This is a simple calculator that can add two numbers
first_number = input("Enter first number: ")
first_number = float(first_number)
second_number = input("Enter Second number ")
second_number = float(second_number)
math_type = input("What math type? ")

if math_type == "+":
    print(float(first_number) + float(second_number))
elif math_type == "-":
    print(float(first_number) - float(second_number))
if math_type == "*":
    print(float(first_number) * float(second_number))
elif math_type == "/":
    print(float(first_number) / float(second_number))
else:
    print("Please type in a valid math type")
