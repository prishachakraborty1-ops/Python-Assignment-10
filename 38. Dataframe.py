import pandas as pd
employees = {
    "emp_id": ["E01", "E02", "E03", "E04", "E05"],
    "emp_name": ["Amit", "Sujay", "Alia", "Sonal", "Niro"],
    "dept": ["IT", "DS", "AI", "IT", "DS"],
    "salary": [10000, 15000, 18000, 14000, 16000]
}

df = pd.DataFrame(employees)

print("Employee DataFrame:")
print(df)

print("\nFirst 2 Employees:")
print(df.head(2))

print("\nLast 2 Employees:")
print(df.tail(2))

print("\nEmployee with Maximum Salary:")
print(df[df["salary"] == df["salary"].max()])