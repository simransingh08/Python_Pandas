# create a bar chart with multiple bars and custom colors
import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [3, 7, 1, 9]
values2 = [5, 2, 8, 4]

# Define the width of the bars
bar_width = 0.35

# Create an array of indices for each category
ind = np.arange(len(categories))

# Create the bar chart
plt.bar(ind, values1, width=bar_width, label='Bar 1', color='blue')
plt.bar(ind + bar_width, values2, width=bar_width, label='Bar 2', color='orange')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Multiple Bars')

# Add x-axis ticks and labels
plt.xticks(ind + bar_width / 2, categories)

# Add legend
plt.legend()

# Display the plot
plt.show()
