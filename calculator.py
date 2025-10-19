"""
Question:

Write a Python program that performs basic arithmetic operations
(addition, subtraction, multiplication, and division) using
user-defined functions and allows continuous input until the
user chooses to exit.
"""


def addition(first_number, second_number):
    number = first_number + second_number
    return number


def subtraction(first_number, second_number):
    number = first_number - second_number
    return number


def multiplication(first_number, second_number):
    number = first_number * second_number
    return number


def division(first_number, second_number):
    number = first_number / second_number
    return number


def enter_number():
    first_number = int(input("Enter Number 1: "))
    second_number = int(input("Enter Number 2: "))
    return first_number, second_number


while True:
    select_option = input("What operation you want perform(+, -, *, /, exit): ").lower()
    valid_option = ("+", "-", "*", "/", "exit")
    if select_option in valid_option:
        if select_option == "+":
            first_number, second_number = enter_number()
            print(f"Sum of two numbers: {addition(first_number, second_number)}")
        elif select_option == "-":
            first_number, second_number = enter_number()
            print(f"Subtraction of two numbers: {subtraction(first_number, second_number)}")
        elif select_option == "*":
            first_number, second_number = enter_number()
            print(f"Multiplication of two numbers: {multiplication(first_number, second_number)}")
        elif select_option == "/":
            first_number, second_number = enter_number()
            print(f"Division of two numbers: {division(first_number, second_number)}")
        elif select_option == "exit":
            print("Program existing! Thanks")
            break
    else:
        print("Enter valid operation!")
