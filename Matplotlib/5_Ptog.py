# creating a simple histogram using Matplotlib:
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
np.random.seed(123)
data = np.random.randn(1000)  # Normally distributed data

# Create a histogram
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Add a grid
plt.grid(True)

# Display the plot
plt.show()
