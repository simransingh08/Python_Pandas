# creating a violin plot with split violins using Seaborn

import seaborn as sns
import matplotlib.pyplot as plt

# Load sample data for demonstration
data = sns.load_dataset("iris")

# Create a violin plot with split violins
plt.figure(figsize=(8, 6))
sns.violinplot(x="species", y="sepal_length", hue="species", data=data, split=True)

# Add labels and title
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Violin Plot with Split Violins')

# Display the plot
plt.show()
