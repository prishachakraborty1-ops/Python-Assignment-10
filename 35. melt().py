import pandas as pd

data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Employee_Name': ['Amit', 'Riya', 'Rahul', 'Priya', 'Neha'],
    'Contact_Kolkata': [9876543210, 9876543211, None, 9876543213, None],
    'Contact_Delhi': [None, 9876543212, 9876543214, None, 9876543215],
    'Project_Kolkata': ['Yes', 'Yes', None, 'Yes', None],
    'Project_Delhi': [None, 'Yes', 'Yes', None, 'Yes']
}

df = pd.DataFrame(data)

print("Wide Format:")
print(df)

long_df = pd.melt(
    df,
    id_vars=['Employee_ID', 'Employee_Name'],
    var_name='Details',
    value_name='Value'
)

print("\nLong Format:")
print(long_df)