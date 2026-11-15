import pandas as pd

data = {
    'Name': ['Anit', 'Rajju', 'Riya'],
    'Dept': ['CSE', 'ECE', 'AIML']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Update department
df.loc[df['Name'] == 'Rajju', 'Dept'] = 'VLSI'

print("\nUpdated DataFrame:")
print(df)