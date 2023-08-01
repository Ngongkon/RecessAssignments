# Advanced topics in python
"""
---summary---
.Regular expressions
.Generators and iterators
.Decorators
.context managers
.multithreading and multiprocessing
"""
# regular expressions
"""
\d:matches any digit (0-9) 
\w:matches any alphanumeric character (a-z, A-Z, 0-9 and underscore)
\s:matches any whitespace character(space, tab,newline)
.:matches any character except newline
*:matches zero or more occurrences of the proceeding character or group
+: matches one or more occurrences of the preceding character or group
?: matches zero or one occurrence of the preceding character or group
[]: matches any character within the square brackets
[^ ]: matches any character not within the square brackets
^: matches the start of a line 
$: matches the end of a line
"""
# Matching and searching
#regex re.match(), re.search(), re.findall()

# Example1 Demonstrating regex | Match first word, match group word, match all numbers
print("................................................................")
print("................................................................")

import re
text = "Hello, my name is Abraham .i am a programmer with 15years of experience"

# Match first word
match = re.search(r"\b\w+\b",text)
if match:
    print("Match:", match.group())

matches = re.findall(r"\d+",text)
print("Matches:", matches)

# Example 2 validate email format or email address
import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True

    else:
        return False   

# Example usage
email = "jeff.geoff98@gmail.com"  
email1 ="jeff.geoff98@gmailcom"    

print(validate_email(email))
print(validate_email(email1))
print("................................................................")
print("................................................................")


# Generators and Iterators
# 'yield' generator
# iterator '__iter__' "__next__ " iterator

def factorial(n):
    # Return the factorial of a number
    if n==0: return 1
    else: return n * factorial(n-1)
# print the factorial of a number from 1 to 10
for i in range(1,10):
    print(factorial(i))    
print("................................................................")
print("................................................................")

# Example3:
# Generate function that yields the square of numbers from 1 to 10
def squares():
    for i in range(1,10):
        yield i ** 2
 # Create an iterator object that yields the square of numbers from 1 to 10

squares_iterator = squares()    
 # print the first 5 squares of numbers from 1 to 10
for i in range(5):
    print(next(squares_iterator))
print("................................................................")
print("................................................................")    

# Decorators @my_decorator
# decotators in python allow to modify the behavior of functions or classes without directly changing their source code
def my_decorator(func):
    def inner():
        print("this is the decorator")
        func()
        
    return inner

@my_decorator
def outer_decorator():   
    print("this is outer decorator")    

outer_decorator()

def decorator_function(original_function):
    def wrapper_function():
        print("Before the function execution")
        original_function()
        print("After the function execution")

    return wrapper_function

@decorator_function
def say_hello():
    print("Hello, world!")

say_hello()
print("................................................................")
print("................................................................")


# Concept of Generators in Python
def number_generator(n):
    for i in range(n):
        yield i

# Using the generator in a loop
for num in number_generator(5):
    print(num)
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator in a loop
for num in fibonacci_generator():
    if num > 100:
        break
    print(num)
print("................................................................")
print("................................................................")
# Concept of multithreading in python
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in 'ABCDE':
        print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()
print("................................................................")
print("................................................................")
# Concept of multiprocessing in Python
import multiprocessing

def square(x):
    return x ** 2

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)
    print(results)
print("................................................................")
print("................................................................")    

# Concept of contex managers in Python
class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Usage of the context manager
with FileContextManager("example.txt", "w") as file:
    file.write("trying the context manager!")
from contextlib import contextmanager

@contextmanager
def file_context_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Usage of the context manager
with file_context_manager("example.txt", "w") as file:
    file.write("Hello, world!")

print("................................................................")
print("................................................................")
# using GUI INTERFACE  FOR EMAIL VALIDATION
import re
import tkinter as tk

def validate_email():
    email = entry.get()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        result_label.config(text="Valid email address.", fg="yellow")
    else:
        result_label.config(text="Invalid email address.", fg="red")

# Create the main window
window = tk.Tk()
window.title("Email Validator")

# Create the entry field
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create the validate button
validate_button = tk.Button(window, text="Validate", command=validate_email)
validate_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the main loop
window.mainloop()
