import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file into a pandas DataFrame
file_path = 'D:/placement-dataset.xlsx'
df = pd.read_excel(file_path)

# Correlation heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

# Bar plot of average IQ and placement by CGPA
grouped_data = df.groupby('cgpa').agg({'iq': 'mean', 'placement': 'mean'}).reset_index()
plt.bar(grouped_data['cgpa'], grouped_data['iq'], label='Average IQ')
plt.bar(grouped_data['cgpa'], grouped_data['placement'], label='Average Placement', alpha=0.7)
plt.xlabel('CGPA')
plt.ylabel('Average Score')
plt.title('Average IQ and Placement by CGPA')
plt.legend()
plt.show()
