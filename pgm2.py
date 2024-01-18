import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a pandas DataFrame
file_path = 'D:/placement-dataset.xlsx'
df = pd.read_excel(file_path)

# Scatter plot of CGPA vs IQ
plt.scatter(df['cgpa'], df['iq'])
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.title('Scatter Plot of CGPA vs IQ')
plt.show()

# Histogram of Placement
plt.hist(df['placement'], bins=20, edgecolor='black')
plt.xlabel('Placement')
plt.ylabel('Frequency')
plt.title('Histogram of Placement')
plt.show()

# Box plot of CGPA
plt.boxplot(df['cgpa'])
plt.ylabel('CGPA')
plt.title('Box Plot of CGPA')
plt.show()
