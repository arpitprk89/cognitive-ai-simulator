# ============================================================
# Smart Calculator with History
# Author: Arpit Pareek | Shrimadhopur, Rajasthan, India
# Purpose: A self-learning Python project demonstrating
#          functions, loops, conditionals, and recursion
# GitHub: github.com/arpitprk89
# ============================================================

import math

history = []  # Store calculation history

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot find square root of negative number!"
    return math.sqrt(a)

def factorial(n):
    """Recursive function to calculate factorial"""
    if n < 0:
        return "Error: Factorial not defined for negative numbers!"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)  # RECURSION used here

def fibonacci(n):
    """Recursive Fibonacci sequence"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    sequence = fibonacci(n - 1)  # RECURSION used here
    sequence.append(sequence[-1] + sequence[-2])
    return sequence

def show_history():
    if not history:
        print("No calculations yet!")
    else:
        print("\n--- Calculation History ---")
        for i, record in enumerate(history, 1):
            print(f"{i}. {record}")
        print("---------------------------\n")

def save_to_history(expression, result):
    history.append(f"{expression} = {result}")

def display_menu():
    print("\n" + "="*45)
    print("       SMART CALCULATOR by Arpit Pareek")
    print("="*45)
    print("1. Addition          (+)")
    print("2. Subtraction       (-)")
    print("3. Multiplication    (*)")
    print("4. Division          (/)")
    print("5. Power             (a^b)")
    print("6. Square Root       (√)")
    print("7. Factorial         (n!)")
    print("8. Fibonacci Series")
    print("9. View History")
    print("0. Exit")
    print("="*45)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def main():
    print("\nWelcome to Smart Calculator!")
    print("Built by Arpit Pareek as a Python learning project.")
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '0':
            print("\nThank you for using Smart Calculator!")
            print("- Arpit Pareek | Rajasthan, India")
            break
            
        elif choice == '1':
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = add(a, b)
            save_to_history(f"{a} + {b}", result)
            print(f"\nResult: {a} + {b} = {result}")
            
        elif choice == '2':
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = subtract(a, b)
            save_to_history(f"{a} - {b}", result)
            print(f"\nResult: {a} - {b} = {result}")
            
        elif choice == '3':
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = multiply(a, b)
            save_to_history(f"{a} * {b}", result)
            print(f"\nResult: {a} * {b} = {result}")
            
        elif choice == '4':
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = divide(a, b)
            save_to_history(f"{a} / {b}", result)
            print(f"\nResult: {a} / {b} = {result}")
            
        elif choice == '5':
            a = get_number("Enter base: ")
            b = get_number("Enter exponent: ")
            result = power(a, b)
            save_to_history(f"{a}^{b}", result)
            print(f"\nResult: {a}^{b} = {result}")
            
        elif choice == '6':
            a = get_number("Enter number: ")
            result = square_root(a)
            save_to_history(f"sqrt({a})", result)
            print(f"\nResult: sqrt({a}) = {result}")
            
        elif choice == '7':
            a = int(get_number("Enter number for factorial: "))
            result = factorial(a)
            save_to_history(f"{a}!", result)
            print(f"\nResult: {a}! = {result}")
            
        elif choice == '8':
            n = int(get_number("How many Fibonacci numbers? "))
            result = fibonacci(n)
            print(f"\nFibonacci Series ({n} terms): {result}")
            
        elif choice == '9':
            show_history()
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
