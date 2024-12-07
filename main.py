import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df["lat"])
print(df["lon"])

plt.scatter(df['lat'].sort_values(), df['lon'].sort_values(), color='blue', label='Data Points')

print(df["lat"].sort_values())
print(df["lon"].sort_values())
plt.title('Scatter Plot of x vs y')  # Title
plt.xlabel('x-axis')  # x-axis label
plt.ylabel('y-axis')  # y-axis label
plt.legend()  # Add legend
plt.grid(True)  # Add gridlines
plt.savefig('scatter_plot.png')  # Save as an image file