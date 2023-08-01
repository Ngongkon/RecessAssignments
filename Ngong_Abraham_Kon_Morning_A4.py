"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""
# Opening a file in write mode
file = open("evening.txt", "w")

# Writing content to the file
file.write("Hello, World!\n")
file.write("This is an example file.\n")
file.write("Writing some text to demonstrate file handling.\n")
file.write("it is a trial file handling.\n")


# Closing the file
file.close()

# Opening the file in read mode and appending the text to the existing file
file = open("evening.txt", "a")
file.write("try to check whether your still exists.\n")
file.close()

# Reading the entire file
file = open("evening.txt", "r")
#print(file.readline()) used for printing the line 
show_details = file.read()
print(show_details)
#for x in file:
#    print(x)

# Closing the file
file.close()

# OR using the with open () function
print("................................................................")
print("BELOW IS THE METHOD OF OPENING THE FILE WITH OPEN () FUNCTION")
try:
    with open("evening.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read the file.")
except Exception as e:
    print("Error:", str(e))


# Deleting the file 
import os as d
print("................................................................")
print("BELOW IS THE METHOD OF DELETING THE FILE")
try:
    filename = "evening.txt"
    d.remove(filename)
    print(f"File '{filename}' successfully deleted.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except PermissionError:
    print(f"Error: Permission denied to delete file '{filename}'.")
except Exception as e:
    print("Error:", str(e))
