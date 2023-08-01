#tuples follow
my_cities = ("kampala","nairobi","dodoma")
print(type(my_cities))
#adding items to the tuple 
z = list(my_cities)
z.append("kigali")
my_cities = tuple(z)
print(my_cities)
#length of the tuple
print(len(my_cities))
#another tuple
my_towns = ("luwero","masindi","soroti","gulu")
#joining the tuples
my_groups = my_cities + my_towns
print(my_groups)
#removing the items from tuples
y = list(my_cities)
y.remove("dodoma")
my_cities = tuple(y)
print(my_cities)