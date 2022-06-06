from art import logo
from os import system

# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    system("clear")
    print(logo)
    continue_operation = True
    for index in operation:
        print(index)

    num1 = float(input("What's the first number?: "))
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operation[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    keep_looping = input(
        f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: "
    )
    if keep_looping == "y":
        continue_operation = True
        system("clear")
        print(logo)
    elif keep_looping == "n":
        continue_operation = False
        calculator()

    second_answer = None
    while continue_operation == True:
        for index in operation:
            print(index)
        operation_symbol = input("Pick an operation from the line above: ")
        num3 = float(input("What is the next number?: "))
        if second_answer == None:
            second_answer = calculation_function(first_answer, num3)
            print(
                f"{first_answer} {operation_symbol} {num3} = {second_answer}"
            )
        elif second_answer != None:
            previous_answer = second_answer
            second_answer = calculation_function(second_answer, num3)
            print(
                f"{previous_answer} {operation_symbol} {num3} = {second_answer}"
            )
        calculation_function = operation[operation_symbol]
        keep_looping = input(
            f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start a new calculation: "
        )
        if keep_looping == "y":
            continue_operation = True
        elif keep_looping == "n":
            continue_operation = False
            calculator()


calculator()
