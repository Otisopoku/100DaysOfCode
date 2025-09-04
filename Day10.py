# Building a simple calculator

import os
from typing import Callable

def clear_terminal() -> None:
    # if on windows, clear the terminal with cls otherwise clear the terminal with clear
    os.system("cls" if os.name == "nt" else "clear")

# My code
# operations = '''
#         +
#         -
#         *
#         /

# '''

# previous_result = 0
# new_operations = True

# def operator(operation, first_num, second_num):
#     if operation == '+':
#         return (first_num + second_num)
#     elif operation == '-':
#         return (first_num - second_num)
#     elif operation == '*':
#         return (first_num * second_num)
#     elif operation == '/':
#         if second_num == 0:
#             raise ZeroDivisionError("Division by zero is not allowed")
#         return (first_num / second_num)
#     else:
#         raise ValueError("Invalid operation")

# while True:
    
#     try:
#         if new_operations:
#             first_num = int(input("What's the first number?: "))
#             print(operations)
#             operation = input("Pick an operation: ")
#             second_num = int(input("What's the next number?: "))
#             result = operator(operation, first_num, second_num)
#             previous_result = result
#             print(f"{first_num:.2f} {operation} {second_num:.2f} = {result:.2f}")
#             choice = input(f"Type 'y' to continue calculating with {previous_result:.2f}, or type 'n' to start a new calculation: ")
#         if choice == 'y':
#             new_operations = False
#             first_num = previous_result
#             print(operations)
#             operation = input("Pick an operation: ")
#             second_num = int(input("What's the next number?: "))
#             result = operator(operation, first_num, second_num)
#             previous_result = result
#             print(f"{first_num:.2f} + {second_num:.2f} = {result:.2f}")
#             choice = input(f"Type 'y' to continue calculating with {previous_result:.2f}, or type 'n' to start a new calculation: ")
#         elif choice == 'n':
#             new_operations = True
#             previous_result = 0
#             clear_terminal()
#         else:
#             raise ValueError("Invalid choice")


#     except ZeroDivisionError as division_e:
#         print(str(division_e))
#     except ValueError as value_e:
#         print(str(value_e))

#AI Code

#using callables avoids a long if/elif statement chain and keeps printing consistent.
OPERATIONS: dict[str, Callable[[float, float], float]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b, # will raise ZeroDivisionError if b == 0
}

def read_number(prompt: str) -> float:
    # prompt until the user enters a valid number. 
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_operation() -> str:
    # prompt until the user picks a valid operation from OPERATIONS
    operations_list = ' '.join(OPERATIONS.keys())
    while True:
        operation = input(f"Pick an operation ({operations_list}): ").strip()
        if operation in OPERATIONS:
            return operation
        print("Invalid operation. Try again.")

def calculator() -> None:
    previous_result: float | None = None # None means start a new calculation

    print("The Simple Calculator")

    while True:
        if previous_result is None:
            first_num = read_number("What is the first number?: ")
        else:
            first_num = previous_result
            print(f"\nContinuing calculations with {first_num:.2f}")

        operation = read_operation()
        second_num = read_number("What is the second number?: ")
        
        if operation == '/' and second_num == 0:
            print("Division by zero is not allowed. Please enter a non-zero number. ")
            continue

        try:
            result = OPERATIONS[operation](first_num, second_num)
        except ZeroDivisionError as err:
            print(str(err))
            continue

        print(f"{first_num:.2f} {operation} {second_num:.2f} = {result:.2f}")

        choice = input(
            f"Type 'y' to continue calculating with {result:.2f}, "
            "type 'n' to start a new calculation, or 'q' to quit: "
        ).strip().lower()

        if choice == 'y':
            previous_result = result
        elif choice == 'n':
            previous_result = None
            clear_terminal()
        elif choice == 'q':
            print("Thank you for using this calculator. GoodBye 👋")
            break
        else:
            # handles the case when the user enters an invalid input
            print("Invalid choice. Starting a new calcuation")
            previous_result = None
            clear_terminal()


if __name__ == "__main__":
    calculator()




