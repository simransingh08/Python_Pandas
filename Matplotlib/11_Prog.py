# creating a polar plot using Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data for demonstration
theta = np.linspace(0, 2*np.pi, 100)
r = 2 + np.sin(6 * theta)

# Create a polar plot
plt.figure(figsize=(8, 8))
plt.polar(theta, r, label='Polar Plot', color='purple')

# Add labels and title
plt.title('Polar Plot Example')

# Add a legend
plt.legend()

# Display the plot
plt.show()
