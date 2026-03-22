"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
    
def request_sanitized_number(prompt: str) -> float:
    """
    Function that prompts the user for a number and ensures that the input is a valid float.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        float: The sanitized number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def request_sanitized_operation(prompt: str) -> str:
    """
    Function that prompts the user for an operation and ensures that the input is valid.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: The sanitized operation entered by the user.
    """
    valid_operations = {"add", "subtract", "multiply", "divide"}
    while True:
        operation = input(prompt).strip().lower()
        if operation in valid_operations:
            return operation
        else:
            print("Invalid input. Please enter 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = request_sanitized_number("Enter the first number: ")
    num2 = request_sanitized_number("Enter the second number: ")
    operation = request_sanitized_operation("Enter the operation (add, subtract, multiply, divide): ")

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")

def test_addition():
    assert simple_calculator("add", 2, 3) == 5      #test for positive numbers
    assert simple_calculator("add", -2, -3) == -5   #test for negative numbers
    assert simple_calculator("add", 2.5, 3.5) == 6  #test for floating point numbers
    assert simple_calculator("add", 0, 0) == 0      #test for zero

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2      #test for positive numbers
    assert simple_calculator("subtract", -5, -3) == -2   #test for negative numbers
    assert simple_calculator("subtract", 5.5, 3.5) == 2  #test for floating point numbers
    assert simple_calculator("subtract", 0, 0) == 0      #test for zero

def test_multiplication():
    assert simple_calculator("multiply", 2, 3) == 6      #test for positive numbers
    assert simple_calculator("multiply", -2, -3) == 6   #test for negative numbers
    assert simple_calculator("multiply", 2.5, 3.5) == 8.75  #test for floating point numbers
    assert simple_calculator("multiply", 0, 0) == 0      #test for zero

def test_division():
    assert simple_calculator("divide", 6, 3) == 2      #test for positive numbers
    assert simple_calculator("divide", -6, -3) == 2   #test for negative numbers
    assert simple_calculator("divide", 7.5, 2.5) == 3.0  #test for floating point numbers
    assert simple_calculator("divide", 0, 1) == 0      #test for zero

def test_division_by_zero():
    try:
        simple_calculator("divide", 5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

def test_invalid_operation():
    try:
        simple_calculator("modulus", 5, 3)
    except ValueError as e:
        assert str(e) == "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."


if __name__ == "__main__":
    main()
