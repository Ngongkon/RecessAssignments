"""
class car:
    def __init__(self, name,model):
        self.name = name
        self.model = model
    def printcar(self):
        print(self.name, "\n", self.model)
mycar = car("toto","telsa")
mycar.printcar()

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 *(self.length + self.width)

my_rect = Rectangle(5,10)
print(my_rect.calculate_area())
print(my_rect.calculate_perimeter())


class Student:
    def __init__(self,name,year,course):
        self.name = name
        self.year = year
        self.course = course
    def display_details(self):
        print("StudentName: " , self.name)
        print("StudentYear: " , self.year)
        print("StudentCourse:", self.course)

my_student = Student("Abram",2020,"software engineering")

my_student.display_details()


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("hello,my name is " , self.name)
        print("am ", self.age, "years old")

my_person = Person("john",20)
my_person1 = Person("peterson",19)
my_person.display()
my_person1.display()
"""

# encapsulation
# key main goal of encapsulations are
"""
1.To hide the implementation details of an object
2.To protect the object from changes
3.To protect the object from external changes
4.code organization and modularity 
"""
# example of encapsulation: with a bank account
"""
class BankAccount:
    def __init__(self, account_number,balance):
        self._account_number = account_number # encapsulate the account number attribute
        self._balance = balance # encapsulate the balance attribute
    def deposit(self, amount):   
        self._balance += amount # encapsulate the deposit 

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("insufficient funds.")
    def get_balance(self):
        return self._balance
my_account = BankAccount("236578675", 1000)    
print(my_account._account_number)   
print(my_account._balance)
my_account.deposit(500)  
print(my_account._balance)
my_account.withdraw(100) 
print(my_account._balance)     
"""

# Execise 2:  convert temperature(37 celsius) from celsius to fahrenheit
""" Convert
class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

   # def set_celsius(self, celsius):
   #     self._celsius = celsius

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32


# Creating an instance of the TemperatureConverter class
converter = TemperatureConverter(37)

# Getting the Celsius temperature
celsius = converter.get_celsius()
print(f"Celsius: {celsius}")

# Getting the Fahrenheit temperature
fahrenheit = converter.get_fahrenheit()
print(f"Fahrenheit: {fahrenheit}")
"""

# Assignment1: show encapsulation with employee information to give a
#pay increment(Salary with employee information to new_salary)e.g from 850000 to 1000000

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary > self._salary:
            self._salary = new_salary
            print("Salary increment is successful.")
        else:
            print("New salary should be greater than the current salary for successful increment.")

# Create an instance of the Employee class
employee = Employee("Ngong Abraham", 90000)

print("----------------------------------------------------------------")
print("----------------------------------------------------------------")


# Get the initial salary
print(employee.get_name(), ",","your Initial Salary is:", employee.get_salary())
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")


# Attempt to set a new salary with encapsulation
employee.set_salary(100000)

# Get the updated salary
print(employee.get_name(), ",","your Updated Salary is:", employee.get_salary())
print("----------------------------------------------------------------")
print("----------------------------------------------------------------")