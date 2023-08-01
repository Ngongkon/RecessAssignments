
class fileMethod:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# sample example below
print("................................................................")
print("This is Context Manager Concept")
with fileMethod('morning.txt', 'r') as f:
   fileOutput = f.read()
   print(fileOutput)

    

print("................................................................")
print(" Database connection with context manager concept")
import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

# sample example below
try:
    with Database('morning.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table_name")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except FileNotFoundError:            
       print("select database file from your computer")

       
print("................................................................")
print("Below is the concept of multthreading and multiprocessing")
import time
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

# Concept of multiprocessing in Python
import multiprocessing

def square(x):
    return x ** 2

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)
    print(results)
