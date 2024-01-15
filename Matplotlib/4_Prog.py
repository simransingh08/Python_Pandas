# creating a scatter plot with Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
np.random.seed(42)
x = np.random.rand(50)
y = 2 * x + 1 + 0.1 * np.random.randn(50)  # Linear relationship with some random noise

# Create a scatter plot
plt.scatter(x, y, label='Scatter Plot', color='green', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Display the plot
plt.show()
