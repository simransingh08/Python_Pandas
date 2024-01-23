# creating a filled area plot with multiple lines using Matplotlib:

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for demonstration
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a filled area plot with multiple lines
plt.figure(figsize=(8, 6))
plt.fill_between(x, y1, label='sin(x)', alpha=0.5)
plt.fill_between(x, y2, label='cos(x)', alpha=0.5)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Filled Area Plot with Multiple Lines')

# Add a legend
plt.legend()

# Display the plot
plt.show()
