# ==================================================
# Week 2 - Logic Challenges (No Guidance)
# ==================================================

# --------------------------------------------------
# Challenge 1: Data cleaning function
# --------------------------------------------------

# You receive data from different sources and it comes with typos.
# Create a function to clean the values before analyze them.

def clean_numeric_values(list_values):
    cleaned_values = []
    converted_value = 0
    for value in list_values:
        try:
            converted_value = int(value)
            cleaned_values.append(converted_value)
        except (TypeError, ValueError):
            continue
    return cleaned_values


data = [10, "20", None, "error", 5, "30", -2]
print(clean_numeric_values(data))

# --------------------------------------------------
# Challenge 2: KPI Calculation function
# --------------------------------------------------

# You need basics metrics for an executive report.
# Create a function to calculate KPIs from a number list.


def calculate_kpis(number_list):
    kpi = {
        "count": 0,
        "total": 0,
        "average": None
    }

    for number in number_list:
        kpi["count"] += 1
        kpi["total"] += number

    if kpi["count"] == 0:
        return kpi

    kpi["average"] = kpi["total"] / kpi["count"]
    return kpi


sales = []
print(calculate_kpis(sales))

# --------------------------------------------------
# Challenge 3: Duplicate detection as a function context
# --------------------------------------------------

# Before to update date in a data base, you must duplicated IDs

def find_duplicates(ids_list):
    duplicated_ids = set()
    no_duplicated_ids = []
    for i in ids_list:
        if i not in no_duplicated_ids:
            no_duplicated_ids.append(i)
        else:
            duplicated_ids.add(i)

    return list(duplicated_ids)

lista = [1,1,1,1,4,5,6,7,4]
print(find_duplicates(lista))

# --------------------------------------------------
# Challenge 4: User validation function
# --------------------------------------------------

# Create a function to filter valid users

def filter_valid_users(users):
    valid_users = []
    for user in users:
        if user["age"] >= 18 and user["age"] <= 125 and user["active"]:
            valid_users.append(user["name"])
            
    return valid_users

users_list = [
{
    "name": "carlos",
    "age": 16,
    "active": True
},
{
    "name": "sara",
    "age": 35,
    "active": False
},
{
    "name": "pedro",
    "age": 125,
    "active": True
}
]

print(filter_valid_users(users_list))