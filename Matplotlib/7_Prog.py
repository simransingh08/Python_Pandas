# creating a stacked bar chart using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [3, 7, 1, 9]
values2 = [5, 2, 8, 4]

# Create a stacked bar chart
fig, ax = plt.subplots()
ax.bar(categories, values1, label='Bar 1', color='blue')
ax.bar(categories, values2, bottom=values1, label='Bar 2', color='orange')

# Add labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart Example')

# Add legend
ax.legend()

# Display the plot
plt.show()
