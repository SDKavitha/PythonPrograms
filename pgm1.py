import pandas as pd

# Load the Excel file into a pandas DataFrame
file_path = 'D:/Anudip/placement-dataset.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())
# Basic statistics of the numerical columns
print(df.describe())

# Correlation between columns
print(df.corr())

# Grouping data by CGPA and calculating average IQ and placement
grouped_data = df.groupby('cgpa').agg({'iq': 'mean', 'placement': 'mean'})
print(grouped_data)
