# ==================================================
# Week 4 - Error handling in Python
# ==================================================

# Data cleaning using try / except
# Convert valid numeric values to integers
# Ignore invalid or non-numeric values safely

# --------------------------------------------------
# Challenge 1: Data cleaning function
# --------------------------------------------------

# Converts values that can be safely cast to int
data = [10, "20", None, "error"]

clean_values = []

for value in data:
    try:
        clean_values.append(int(value))
    except (ValueError, TypeError):
        continue

print(clean_values)

# --------------------------------------------------
# Challenge 2: Invalid Data Counter
# --------------------------------------------------

#Measure data quality by counting invalid values.
data = [5, "Leonardo", "Medellin", None, 10]

invalid_count = 0
for value in data:
    try:
        converted = int(value)
    except (TypeError, ValueError):
        invalid_count += 1
        
print(invalid_count)

# --------------------------------------------------
#Exercise 3: Function with Error Handling
# --------------------------------------------------

#Create a reusable data cleaning function.
data = [10, "20", None, "error", 30]

def data_quality_report(values):
    converted = 0
    result = {"valid_records": 0,
    "invalid_records": 0,
    "total_records": 0}
    
    for value in values:
        try:
            converted = int(value)
            result["valid_records"] += 1
        except (TypeError, ValueError):
            result["invalid_records"] += 1
        finally:
            result["total_records"] += 1
    return result

print(data_quality_report(data))
