"""
Exception handling in Python allows you to handle errors or exceptions that may occur during the execution 
of a program. This helps in gracefully managing unexpected situations and prevents the program from crashing. 
The key components of exception handling in Python are:

try, except, and else blocks: The try block is used to enclose the code that might raise an exception. 
If an exception occurs within the try block, it is caught and handled in the corresponding except block. 
The else block, if present, executes if no exception occurs in the try block.

except clause: It catches and handles specific exceptions that occur in the try block. You can specify the type 
of exception to catch or use a generic except block to catch any unexpected exception.


finally block: The finally block, if present, is always executed, regardless of whether an exception 
occurred or not. It is generally used for cleanup operations like closing files or releasing resources.
"""

print("................................................................")
print("EXCEPTION HANDLING USING FUNCTION::")
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both inputs should be numbers.")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")

# Test the function with different inputs
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "2")

print("................................................................")
print("REQUEST THE USER TO ENTER THE VALUES::")


# TRYING WITH USER INPUTS
def divide_numbers():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except Exception as e:
        print("Error:", str(e))
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")

# Call the function
divide_numbers()
print("................................................................")
print("................................................................")
