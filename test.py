import abc
import argparse
import re
import time
import threading
import multiprocessing
import random
import string
import requests
import unittest
import pytest
from typing import List, Dict
from contextlib import contextmanager
from datetime import datetime

# 61. Class Basics
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Example usage:
person = Person("John", 30)
person.greet()

# 62. Class Inheritance
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Example usage:
dog = Dog()
dog.speak()

# 63. Encapsulation
class BankAccount:
    def __init__(self):
        self._balance = 0
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount

# 64. Polymorphism
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")

# Example usage:
shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()

# 65. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

# 66. Abstract Class
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# 67. Property Decorator
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

# 68. Command-Line Tool
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Input file path')
    parser.add_argument('--verbose', action='store_true')
    return parser

# 69. Flatten Nested List
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# 70. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 71. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# 72. BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 73. DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 74. Path Finding in Grid
def has_path(grid):
    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]):
            return False
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return True
        return grid[i][j] == 0 and (dfs(i+1, j) or dfs(i, j+1))
    
    return dfs(0, 0)

# 75. Phone Number Regex
def validate_phone(text):
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)

# 76. Email Extraction
def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

# 77. Decorator for Timing
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

# 78. Context Manager
@contextmanager
def timer_context():
    print("Starting...")
    start = time.time()
    yield
    end = time.time()
    print(f"Finished! Took {end - start:.2f} seconds")

# 79. Threading Example
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)

def print_letters():
    for c in 'ABCDE':
        print(c)
        time.sleep(0.5)

# Example usage:
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t1.start()
t2.start()

# 80. Multiprocessing Example
def process_data(number):
    return number * number

def main():
    with multiprocessing.Pool(4) as pool:
        result = pool.map(process_data, range(10))
    print(result)

# 81. Random Password Generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# 82. Simple HTTP GET Request
def fetch_data(url):
    response = requests.get(url)
    return response.json()

# 83. Type Hints
def add_numbers(a: int, b: int) -> int:
    return a + b

def get_user_info(name: str, age: int) -> Dict[str, any]:
    return {"name": name, "age": age}

# 84. Unit Testing
class Calculator:
    def add(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

# 85. pytest Example
def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

@pytest.fixture
def calculator():
    return Calculator()

def test_with_fixture(calculator):
    assert calculator.add(2, 3) == 5

# 86. Sorting List of Dictionaries
def sort_by_age(people):
    return sorted(people, key=lambda x: x['age'])

# Example usage:
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]
sorted_people = sort_by_age(people)