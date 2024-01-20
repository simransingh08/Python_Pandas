# creating a violin plot using Matplotlib and Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate random data for demonstration
np.random.seed(123)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Create a violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(data=data, inner="quartile", palette="pastel")

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Violin Plot Example')

# Display the plot
plt.show()
