# creating a horizontal bar chart with error bars using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [3, 7, 5, 9]
errors = [0.5, 1, 0.7, 1.2]

# Create a horizontal bar chart with error bars
plt.figure(figsize=(8, 6))
plt.barh(categories, values, xerr=errors, color='skyblue', edgecolor='black', capsize=5)

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart with Error Bars')

# Display the plot
plt.show()
