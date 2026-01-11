"""
Week 01 - Python Basics
Topic: Variables, Data Types and Type Casting

This script covers:
- Dynamic and strong typing
- Variable naming conventions
- Type annotations
- Type casting
- Basic built-in functions
- Built-in Data Structures
- Simple practice exercises
"""

# --------------------------------------------------
# Variables and Dynamic Typing
# --------------------------------------------------

age = 19
print(type(age))

age = "Carlos"
print(type(age))

# Strong typing: Python does not perform implicit type conversions
# Uncommenting the following line will raise a TypeError
# print(10 - "2")

my_name = "Leonardo"
print(my_name)

# f-strings (formatted string literals)
print(f"My name is {my_name} and I am {age} years old")

# --------------------------------------------------
# Naming Conventions
# --------------------------------------------------

snake_case_variable = "recommended"
PascalCaseVariable = "used for classes"

PI_CONSTANT = 3.14  # Constant naming convention

# --------------------------------------------------
# Type Annotations (not enforced at runtime)
# --------------------------------------------------

is_user_logged_in: bool = True
print(is_user_logged_in)

# Dynamic typing allows reassignment with a different type
is_user_logged_in = 42
print(is_user_logged_in)

# --------------------------------------------------
# Type Casting (Type Conversion)
# --------------------------------------------------

print("\nType Casting Examples")

print(type(int("100")))       # str -> int
print("100" + str(5))         # int -> str
print(bool(0))                # False
print(bool(1))                # True
print(int(2.5))               # 2 (truncates decimal part)
print(round(2.6))             # 3

# round() rounds to the nearest even number when the decimal is .5
print(round(3.5))             # 4
print(round(4.5))             # 4

# --------------------------------------------------
# Built-in Data Structures
# --------------------------------------------------

print("\nBuilt-in Data Structures")

# Boolean
is_active = True
has_permission = False
print(is_active, has_permission)
print(type(is_active))

# List (ordered, mutable)
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers[0] = 10
print(numbers)
print(type(numbers))

# Tuple (ordered, immutable)
coordinates = (4.5, 6.2)
print(coordinates)
print(type(coordinates))

# Dictionary (key-value pairs)
user = {
    "name": "Leonardo",
    "age": 24,
    "city": "Medellín",
    "is_active": True
}

print(user)
print(user["name"])
print(type(user))

# Set (unordered, unique elements)
unique_numbers = {1, 2, 3, 3, 4, 5}
unique_numbers.add(6)
print(unique_numbers)
print(type(unique_numbers)) # Result: {1, 2, 3, 4, 5, 6}

# --------------------------------------------------
# Practice Exercises (Executed Examples)
# --------------------------------------------------

print("\nExercise 1: Print messages")
print("My city is Medellín")
print("My name is Leonardo")

print("\nExercise 2: Data types")
a = 15
b = 3.14159
c = "Hello world"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nExercise 3: Casting")
string_number = "12345"
decimal_number = 3.99

print(int(string_number))
print(float(string_number))
print(int(decimal_number))  # Only the integer part is kept

print("\nExercise 4: Variables and f-strings")
my_name = "Leonardo"
age = 24
height = 1.70

print(f"My name is {my_name}, I am {age} years old and my height is {height} meters")

print("\nExercise 5: Numbers and operations")
PI = 3.1416
rounded_pi = round(PI)
result = rounded_pi // 2

print(result)  # Expected output: 1

print("\nExercise 5: Mutable vs Immutable objects")

# ---------------- Mutable ----------------
numbers_list = [1, 2, 3]
print("Original list ID:", id(numbers_list))

numbers_list.append(4)
print("Modified list:", numbers_list)
print("List ID after modification:", id(numbers_list))
# The ID remains the same because lists are mutable

# ---------------- Immutable ----------------
coordinates = (7.6, 5.8)
print("\nOriginal tuple ID:", id(coordinates))

coordinates = (10, 30)
print("New tuple:", coordinates)
print("New tuple ID:", id(coordinates))
# A new object is created because tuples are immutable

