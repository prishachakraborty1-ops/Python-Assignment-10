import pandas as pd

data = {
    'Name': ['Amit', 'Prisha'],
    'Math': [80, 90],
    'Science': [85, 95]
}

df = pd.DataFrame(data)
df = df.set_index('Name')

print("Original DataFrame:")
print(df)

print("\nAfter Stack:")
print(df.stack())

print("\nAfter Unstack:")
print(df.stack().unstack())