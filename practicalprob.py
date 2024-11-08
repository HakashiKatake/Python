

### 1) Arithmetic Operators

a, b = 10, 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)


### 2) Greatest Number Among Three Numbers

def greatest(a, b, c):
    return max(a, b, c)
print("Greatest:", greatest(5, 10, 3))

### 3) Sum of Numbers from 5 to 15

total = sum(range(5, 16))
print("Sum from 5 to 15:", total)


### 4) Factorial of a Number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial:", factorial(5))


### 5) Print Pattern

for i in range(1, 6):
    print("*" * i)


### 6) Sum and Average of Array

arr = [1, 2, 3, 4, 5]
total = sum(arr)
average = total / len(arr)
print("Sum:", total, "Average:", average)


### 7) Check Prime Number

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Prime:", is_prime(17))

### 8) Recursive Fibonacci Series

def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci(n - 1, b, a + b)
fibonacci(10)


### 9) Check Palindrome

def is_palindrome(s):
    return s == s[::-1]
print("Palindrome:", is_palindrome("madam"))


### 10) Sum of Variable-Length Arguments

def sum_varargs(*args):
    return sum(args)
print("Sum:", sum_varargs(1, 2, 3, 4, 5))


### 11) Remove Duplicates from a List

lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = list(set(lst))
print("Unique list:", unique_lst)


### 12) Square of Numbers from 1 to 10 using List Comprehension

squares = [x ** 2 for x in range(1, 11)]
print("Squares:", squares)


### 13) Element-wise Sum of Tuples

tuples = [(1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1)]
result = tuple(map(sum, zip(*tuples)))
print("Element-wise sum:", result)


### 14) Unique Items from Two Sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
unique_items = set1.symmetric_difference(set2)
print("Unique items:", unique_items)


### 15) Dictionary Comprehension for Even Ages

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_age_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}
print("Even age dict:", even_age_dict)


### 16) Remove Spaces from String

string = "Python is very easy"
no_spaces = string.replace(" ", "")
print("String without spaces:", no_spaces)


### 17) Simple Interest Calculation

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest: {:.2f}".format(simple_interest))


### 18) Circle Class with Area and Perimeter

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())


### 19) Inheritance in Person and Student Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, rollno, stream):
        super().__init__(name, age)
        self.rollno = rollno
        self.stream = stream
    
    def display(self):
        print("Name:", self.name, "Age:", self.age, "Roll No:", self.rollno, "Stream:", self.stream)

s = Student("Alice", 20, 101, "Science")
s.display()


### 20) Count Words in a Text File

with open("textfile.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
print("Word count:", word_count)


### 21) Handle ZeroDivisionError with Exception Handling

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")


### 22) Lambda in `map()` Function

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)


### 23) Lambda in `filter()` Function
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


### 24) Class Method and Static Method

class Example:
    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls):
        print("This is a class method.")

    @staticmethod
    def static_method():
        print("This is a static method.")

Example.class_method()
Example.static_method()


### 25) GUI Application to Add Two Numbers

import tkinter as tk

def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result.set(num1 + num2)

root = tk.Tk()
root.title("Add Numbers")

entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
result = tk.StringVar()
label_result = tk.Label(root, textvariable=result)
label_result.pack()

button_add = tk.Button(root, text="Add", command=add_numbers)
button_add.pack()

root.mainloop()
