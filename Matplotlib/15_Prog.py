# creating a grouped bar chart with Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [3, 7, 5, 9]
values2 = [5, 2, 8, 4]

# Set the width of the bars
bar_width = 0.35

# Create an array of indices for each category
ind = np.arange(len(categories))

# Create a grouped bar chart
plt.figure(figsize=(8, 6))
plt.bar(ind - bar_width/2, values1, width=bar_width, label='Group 1', color='skyblue')
plt.bar(ind + bar_width/2, values2, width=bar_width, label='Group 2', color='orange')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Chart Example')

# Add x-axis ticks and labels
plt.xticks(ind, categories)

# Add legend
plt.legend()

# Display the plot
plt.show()
