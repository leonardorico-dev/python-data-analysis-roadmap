# ==================================================
# Week 2 - Control Flow and Logic
# ==================================================

# --------------------------------------------------
# Operators
# --------------------------------------------------

# Arithmetic operators
a = 10
b = 3

print("Arithmetic Operators")
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation

# Comparison operators
print("\nComparison Operators")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators
print("\nLogical Operators")
is_adult = True
has_id = False

print(is_adult and has_id)
print(is_adult or has_id)
print(not is_adult)

# Assignment operators
print("\nAssignment Operators")
counter = 0
counter += 1
counter -= 1
counter *= 2
counter /= 2
print(counter)

# Membership and identity operators
print("\nMembership and Identity Operators")
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)
print(10 not in numbers)

x = 10
y = 10
print(x is y)
print(x is not y)

# --------------------------------------------------
# Conditional Statements
# --------------------------------------------------

print("\nConditional Statements")

age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Nested condition example
score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs improvement")

# --------------------------------------------------
# Loops
# --------------------------------------------------

print("\nFor Loop Example")

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

print("\nWhile Loop Example")

counter = 0
while counter < 5:
    print(counter)
    counter += 1

# --------------------------------------------------
# Loop Control Statements
# --------------------------------------------------

print("\nLoop Control Statements")

for number in range(1, 11):
    if number == 5:
        continue  # Skip this iteration
    if number == 8:
        break     # Exit the loop
    print(number)

# pass statement (placeholder)
if True:
    pass

# --------------------------------------------------
# Built-in Functions for Iteration
# --------------------------------------------------

print("\nBuilt-in Functions")

values = [10, 20, 30, 40]

print(len(values))
print(sum(values))
print(min(values))
print(max(values))

for index, value in enumerate(values):
    print(index, value)
