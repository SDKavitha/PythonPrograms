import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a pandas DataFrame
file_path = 'C:/Users/sivar/OneDrive/Desktop/placement-dataset.xlsx'
df = pd.read_excel(file_path)

# Group data by IQ and calculate total placement for each IQ level
iq_placement_total = df.groupby('iq')['placement'].sum().reset_index()

# Bar chart
plt.bar(iq_placement_total['iq'], iq_placement_total['placement'])
plt.xlabel('IQ')
plt.ylabel('Total Placement')
plt.title('Total Placement based on IQ')
plt.show()
