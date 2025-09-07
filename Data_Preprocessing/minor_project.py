import pandas as pd
import numpy as np

# 1. Load the data in dataframe (Pandas)
data = pd.read_csv("Data_Preprocessing/melb_data.csv")

# 2. Handle inappropriate data

data = data.drop_duplicates()

data = data[data['Price'] > 0]
data = data[data['Bedroom2'] > 0]

# 3. Handle the missing data
missing_data_count = data.isnull().sum()
num_cols = data.select_dtypes(include=[np.number]).columns
for col in num_cols:
        data[col] = data[col].fillna(data[col].median())
cat_cols = data.select_dtypes(include=[object]).columns
for col in cat_cols:
        data[col] = data[col].fillna(data[col].mode()[0])
# 4. Handle categorical data
data = pd.get_dummies(data, columns=cat_cols, drop_first=True)
print(data.info())
print(data.head())
