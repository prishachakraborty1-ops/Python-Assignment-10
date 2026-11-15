import pandas as pd
import numpy as np
students = {
    "roll": [1, 2, 3, 4, 5],
    "name": ["Amit", "Rhea", "Sima", "Raju", "Rohita"],
    "dept": ["CSE", "IT", np.nan, "ESE", np.nan],
    "marks": [90, np.nan, 80, 85, 95]
}

df = pd.DataFrame(students)

print("Original DataFrame:")
print(df)

print("\nColumns with Null Values:")
print(df.isnull().sum())

df.loc[df["name"] == "Sima", "dept"] = "CSE"

print("\nAfter Filling Sima's Department:")
print(df)

df = df.dropna(subset=["dept"])

print("\nAfter Deleting Rohita's Null Value:")
print(df)