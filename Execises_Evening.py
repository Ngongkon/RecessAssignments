

#Exercise1 (Lists)
print("----------------------------------------------------------------")

print("----------------------------------------------------------------")

print("EXECISE 1 (LISTS)")
#1
names = ["lilian", "Abraham", "samuel", "margret", "mary"]
second_item = names[1]
print(second_item)
#2
names = ["lilian", "Abraham", "samuel", "margret", "mary"]
names[0] = "Alex"
print(names)
#3
names = ["lilian", "Abraham", "samuel", "margret", "mary"]
names.append("johnson")
print(names)
#4
names = ["lilian", "Abraham", "samuel", "margret", "mary"]
names.insert(2, "Bathel")
print(names)
#5
names = ["lilian", "Abraham", "samuel", "margret", "mary"]
del names[3]
print(names)
#6
names = ["lilian", "Abraham", "samuel", "margret", "mary"]
last_item = names[-1]
print(last_item)
#7
new_list = [1, 2, 3, 4, 5, 6, 7]
items = new_list[2:5]
print(items)
#8
countries = ["USA", "Canada", "Australia", "Germany", "Japan"]
countries_copy = countries.copy()
print(countries_copy)
#9
countries = ["USA", "Canada", "Australia", "Germany", "Japan"]
for country in countries:
    print(country)
#10
animal_names = ["Tiger", "Lion", "Elephant", "Giraffe", "Monkey"]
ascending_order = sorted(animal_names)
descending_order = sorted(animal_names, reverse=True)
print(ascending_order)
print(descending_order)
#11
animal_names = ["Tiger", "Lion", "Elephant", "Giraffe", "Monkey"]
names_with_a = [name for name in animal_names if 'a' in name.lower()]
print(names_with_a)
#12
first_names = ["John", "Jane", "Alice"]
last_names = ["Doe", "Smith", "Johnson"]
full_names = first_names + last_names
print(full_names)

print("----------------------------------------------------------------")

print("----------------------------------------------------------------")


#Exercise2 (Tuples)

print("EXECISE 2 (TUPLES)")
#1
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print(favorite_brand)
#2
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print(second_last_item)
#3
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print(x)
#4
x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)
print(x)
#5
x = ("samsung", "iphone", "tecno", "redmi")
for phone in x:
    print(phone)
#6
x = ("samsung", "iphone", "tecno", "redmi")
x = x[1:]
print(x)
#7
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(uganda_cities)
#8
x = ("samsung", "iphone", "tecno", "redmi")
brand1, brand2, brand3, brand4 = x
print(brand1, brand2, brand3, brand4)
#9
uganda_cities = ("Kampala", "Entebbe", "Jinja", "Mbarara")
cities = uganda_cities[1:4]
print(cities)
#10
first_names = ("John", "Jane", "Alice")
last_names = ("Doe", "Smith", "Johnson")
full_names = first_names + last_names
print(full_names)
#11
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)
#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print(count)

print("----------------------------------------------------------------")

print("----------------------------------------------------------------")

#Exercise3 (Sets)

print("EXECISE 3 (SETS)")
#1
beverages = set(["coffee", "tea", "juice"])
print(beverages)
#2
beverages.add("water")
beverages.update(["soda", "smoothie"])
print(beverages)
#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")
#4
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)
#5
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)
#6
mySet = {"apple", "banana", "orange", "grape"}
myList = ["pear", "kiwi"]
mySet.update(myList)
print(mySet)
#7
ages = {25, 30, 35}
first_names = {"John", "Jane", "Alice"}
joined_set = ages.union(first_names)
print(joined_set)

print("----------------------------------------------------------------")

print("----------------------------------------------------------------")

#Exercise4 (Strings)

print("EXECISE 4 (STRINGS)")
#1
integer_variable = 10
string_variable = "Hello"
concatenated_variable = str(integer_variable) + string_variable
print(concatenated_variable)
#2
txt = " Hello, Uganda! "
stripped_txt = txt.strip()
print(stripped_txt)
#3
txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print(uppercase_txt)
#4
txt = "Hello, Uganda!"
replaced_txt = txt.replace('U', 'V')
print(replaced_txt)
#5
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)
#6
x = 'All "Data Scientists" are cool!'
print(x)

print("----------------------------------------------------------------")

print("----------------------------------------------------------------")
#Exercise5 (Dictionaries)

print("EXECISE 5 (DICTIONARIES)")
#1
Shoes = {"brand": "Nick", "color": "black", "size": 40}
shoe_size = Shoes["size"]
print(shoe_size)
#2
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes["brand"] = "Adidas"
print(Shoes)
#3
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes["type"] = "sneakers"
print(Shoes)
#4
Shoes = {"brand": "Nick", "color": "black", "size": 40}
keys_list = list(Shoes.keys())
print(keys_list)
#5
Shoes = {"brand": "Nick", "color": "black", "size": 40}
values_list = list(Shoes.values())
print(values_list)
#6
Shoes = {"brand": "Nick", "color": "black", "size": 40}
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")
#7
Shoes = {"brand": "Nick", "color": "black", "size": 40}
for key, value in Shoes.items():
    print(key, ":", value)
#8
Shoes = {"brand": "Nick", "color": "black", "size": 40}
del Shoes["color"]
print(Shoes)
#9
Shoes = {"brand": "Nick", "color": "black", "size": 40}
Shoes.clear()
print(Shoes)
#10
original_dict = {"key1": "value1", "key2": "value2"}
copy_dict = original_dict.copy()
print(copy_dict)
#11
nested_dict = {
    "student1": {"name": "Abraham", "age": 25},
    "student2": {"name": "peter", "age": 30},
    "student3": {"name": "mary", "age": 35}
}

for person, details in nested_dict.items():
    print("Person:", person)
    for key, value in details.items():
        print(key, ":", value)
    print()

