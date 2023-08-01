#sets
my_sets = {20,21,22,23,24}
#type 
print(type(my_sets))
#accessing items in the sets
for x in my_sets:
  print(x)
#adding items to the set
my_sets.add(25)
print(my_sets)
#removing items
my_sets.remove(22)
print(my_sets)
#another set
my_set2 ={"one","two","three","four"}
#joining sets using union() function
set3 = my_sets.union(my_set2)
print(set3)
#joining sets using update() function
my_sets.update(my_set2)
print(my_sets)
