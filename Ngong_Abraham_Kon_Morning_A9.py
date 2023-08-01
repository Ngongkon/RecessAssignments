# Inheritance 

"""
#Inheritance is a mechanism that allows a class (child class) to inherit the properties and methods 
#of another class (parent class). The child class can then extend or modify the inherited behavior. 
#In Python, you can create an inheritance relationship between classes by specifying the parent class in 
#parentheses after the child class name when defining the child class.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal("Animal")
animal.speak()  

dog = Dog("Buddy")
dog.speak()  

# Polymorphism allows us to write code that can work with different objects
# method overriding occurs when a derived class,subclass,(child class),provides its own
# implementation of a method that is already defined in its subclass
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Creating objects of the subclasses
dog = Dog()
cat = Cat()

# Calling the overridden method
dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!



# Abstraction
# Allow you to focus on essential features and hide them unnecessary details
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

    def move(self):
        return "Running"

class Cat(Animal):
    def sound(self):
        return "Meow!"

    def move(self):
        return "Jumping"

# Creating objects of the concrete classes
dog = Dog()
cat = Cat()

# Calling methods on the objects
print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!
print(dog.move())   # Output: Running
print(cat.move())   # Output: Jumping
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage example
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
"""


# Assignment 1: create a receipt printing program with GUI interface,
# a more advanced detail earns you more points
import abc
import tkinter as tk

class Item(abc.ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abc.abstractmethod
    def get_description(self):
        pass

    def get_price(self):
        return self.price

class Product(Item):
    def get_description(self):
        return "Product: " + self.name

class Service(Item):
    def get_description(self):
        return "Service: " + self.name

class Receipt:
    def __init__(self):
        self.customer_name = ""
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.get_price() for item in self.items)

    def generate_receipt(self):
        text = "Customer Name: {}\n\n".format(self.customer_name)
        for item in self.items:
            text += "{} = Ugsh{}\n".format(item.get_description(), item.get_price())
        text += "\nTotal: Ugsh{}".format(self.calculate_total())
        return text

class ReceiptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printing Program")

        self.receipt = Receipt()

        self.customer_name_label = tk.Label(root, text="Customer Name:")
        self.customer_name_label.pack()
        self.customer_name_entry = tk.Entry(root)
        self.customer_name_entry.pack()

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()
        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.type_label = tk.Label(root, text="Type:")
        self.type_label.pack()
        self.type_var = tk.StringVar(root)
        self.type_var.set("Product")
        self.type_option = tk.OptionMenu(root, self.type_var, "Product", "Service")
        self.type_option.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.receipt_button = tk.Button(root, text="Print Your Receipt Details", command=self.generate_receipt)
        self.receipt_button.pack()

        self.text = tk.Text(root)
        self.text.pack()

    def add_item(self):
        item = self.item_entry.get()
        price = float(self.price_entry.get())
        item_type = self.type_var.get()

        if item_type == "Product":
            receipt_item = Product(item, price)
        else:
            receipt_item = Service(item, price)

        self.receipt.add_item(receipt_item)
        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def generate_receipt(self):
        self.receipt.customer_name = self.customer_name_entry.get()
        text = self.receipt.generate_receipt()
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, text)
# Create the Tkinter application window
root = tk.Tk()
# Create the ReceiptApp instance
app = ReceiptApp(root)
# Run the Tkinter event loop
root.mainloop()