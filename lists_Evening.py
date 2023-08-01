#list of alphabetic characters in python
my_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(my_list)
#acessing my_list using positive indices from index 2 to the end of my_list
print(my_list[2:])
#acessing my_list using negative indices 
print(my_list[-2:])
#print the number of items in my_list using len() function
print(len(my_list))
#getting data type using type() function
print(type(my_list))
my_list2 = [1,2,3,4,5,6,7,8,9]
#joining two lists 
my_list3 = my_list + my_list2
print(my_list3)
#joining two lists using extend() method
my_list.extend(my_list2)
print(my_list)
#removing items from the lists using remove() method
my_list.remove("f")
print(my_list)