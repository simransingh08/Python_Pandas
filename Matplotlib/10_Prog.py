# creating a heatmap using Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate random data for demonstration
np.random.seed(42)
data = np.random.rand(5, 5)

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, cmap='viridis', cbar=True)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Heatmap Example')

# Display the plot
plt.show()
