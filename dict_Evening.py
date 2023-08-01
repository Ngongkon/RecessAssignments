#used to store data values in key:value pairs 
#dictionaries are ordered,changeable but do not allow duplicates
#Dict can have items of different types
mydict = {
    "phone":"iphone",
    "iphonemodel":"iphone15",
    "year": 2023
}
print(mydict)
#length of a dictionary
print(len(mydict))
#data type
print(type(mydict))
#Access Dictionary items
z = mydict["year"]
print(z)
x = mydict.get("phone")
print(x)
#getting keys in a dictionary
b = mydict.keys()
print(b)
#Execise one:use the values() method to return a list of all values in the dictionary
# Sample dictionary
fruits = {
    'apple': 5,
    'banana': 3,
    'orange': 2
}

# Get a list of all values in the dictionary
fruit_values = list(fruits.values())

# Print the list of values
print(fruit_values)

#execise two: to check if a key does exist in the dictionary
# Sample dictionary
fruits = {
    'apple': 5,
    'banana': 3,
    'orange': 2
}

# Checking if a key exists
if 'banana' in fruits:
    print("Banana exists in the dictionary.")

if 'grape' not in fruits:
    print("Grape does not exist in the dictionary.")
# Sample dictionary
fruits = {
    'apple': 5,
    'banana': 3,
    'orange': 2
}

# Checking if a key exists
if fruits.get('banana') is not None:
    print("Banana exists in the dictionary.")

if fruits.get('grape') is None:
    print("Grape does not exist in the dictionary.")

#execise three: give an example on how to change dictionary items,how to update
# Initial dictionary
fruits = {
    'apple': 5,
    'banana': 3,
    'orange': 2
}

# Changing the value of an item
fruits['banana'] = 6

# Printing the updated dictionary
print(fruits)
# Initial dictionary
fruits = {
    'apple': 5,
    'banana': 3
}

# Dictionary with updates
updates = {
    'banana': 6,
    'orange': 2
}

# Updating the dictionary
fruits.update(updates)

# Printing the updated dictionary
print(fruits)

#execise four:give an example on how to add dictionary items,how to remove dictionary items
# Initial dictionary
fruits = {
    'apple': 5,
    'banana': 3
}

# Adding a new item
fruits['orange'] = 2

# Modifying an existing item
fruits['apple'] = 7

# Printing the updated dictionary
print(fruits)
# Initial dictionary
fruits = {
    'apple': 5,
    'banana': 3,
    'orange': 2
}

# Removing an item using del
del fruits['banana']

# Removing an item using pop
removed_value = fruits.pop('orange')

# Printing the updated dictionary and removed value
print(fruits)
print(removed_value)

#execise five: give an example on how you can loop through a dictionary and also how to nest dictionaries 
# Sample dictionary
fruits = {
    'apple': 5,
    'banana': 3,
    'orange': 2
}

# Looping through the dictionary
for fruit, quantity in fruits.items():
    print(f"There are {quantity} {fruit}s.")
# Sample nested dictionary
students = {
    'Alice': {
        'age': 20,
        'grade': 'A'
    },
    'Bob': {
        'age': 19,
        'grade': 'B'
    },
    'Charlie': {
        'age': 21,
        'grade': 'A+'
    }
}

# Accessing nested dictionary values
print(students['Alice']['age'])  # Output: 20
print(students['Bob']['grade'])  # Output: B
