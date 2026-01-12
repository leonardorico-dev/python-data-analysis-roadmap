# ==================================================
# Week 2 - Logic Challenges (No Guidance)
# ==================================================

# --------------------------------------------------
# Challenge 1: Number Classification
# --------------------------------------------------

# Given a list of integers:
# - Ignore negative numbers
# - If the number is 0, print it explicitly
# - For positive numbers, indicate whether they are even or odd


numbers = [3, 7, 10, 15, 22, 0, -4]

for number in numbers:
    if number < 0:
        print("The number is negative")
    elif number == 0:
        print("The number is 0")
    else:
        if number % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")

# --------------------------------------------------
# Challenge 2: User Validation
# --------------------------------------------------
# You have a list of users represented as dictionaries.

# Rules:
# - Ignore users with invalid age
# - A valid user must:
# - Be 18 or older
# - Be active
# - Print the name of each valid user
# - Count how many valid users exist


users = [
    {"name": "Ana", "age": 25, "active": True},
    {"name": "Luis", "age": 17, "active": True},
    {"name": "Carlos", "age": 32, "active": False},
    {"name": "Sofia", "age": -5, "active": True},
]

valid_users = 0
for user in users:
    if user["age"] < 0:
        continue
    elif user["age"] >= 18 and user["active"]:
        valid_users += 1
        print(user["name"])
        
print(valid_users)

# --------------------------------------------------
# Challenge 3: Access Control Simulation
# --------------------------------------------------

# Simulate a simple access control system.

# Rules:
# - Access is granted only if:
#   - The user has an ID AND
#   - (The user has permission OR is an employee)

has_id = True
has_permission = False
is_employee = True

if has_id and (has_permission or is_employee):
    print("Access is granted")
else:
    print("Access is denied")

# --------------------------------------------------
# Challenge 4: Basic Data Cleaning
# --------------------------------------------------

# Given a list with mixed values:
# - Ignore non-numeric values
# - Convert numeric strings to integers
# - Calculate:
#   - Total number of valid values
#   - Sum of valid values
#   - Average


data = [10, "20", None, 5, "error", 30]

count_numbers = 0
sum_numbers = 0
for value in data:
    try:
        converted_value = int(value)
        count_numbers += 1
        sum_numbers += converted_value
    except (ValueError, TypeError):
        continue
        
print("The count of the values is", count_numbers)
print("The sum of the values is", sum_numbers)
print("The avarage is", sum_numbers/count_numbers)

# --------------------------------------------------
# Challenge 5: Controlled Loop
# --------------------------------------------------

# - Iterate from 1 to 50
# - Stop the loop when a number divisible by both 5 and 7 is found
# - Print all numbers before stopping


for number in range(1,50):
    if number % 5 == 0 and number % 7 == 0:
        break
    else:
        print(number)

# --------------------------------------------------
# Challenge 6: Duplicate Detection
# --------------------------------------------------

# Given a list of IDs:
# - Detect duplicated values
# - Print only the duplicated IDs
# - Do not use external libraries

ids = [101, 102, 103, 101, 104, 102, 105]

seen_ids = set()
duplicate_ids = set()

for id_value in ids:
    if id_value in seen_ids:
        duplicate_ids.add(id_value)
    else:
        seen_ids.add(id_value)
        
print(list(duplicate_ids))