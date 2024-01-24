# creating a stacked area plot using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for demonstration
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a stacked area plot
plt.figure(figsize=(8, 6))
plt.stackplot(x, y1, y2, labels=['sin(x)', 'cos(x)'], baseline='zero', alpha=0.7)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Stacked Area Plot')

# Add a legend
plt.legend()

# Display the plot
plt.show()
