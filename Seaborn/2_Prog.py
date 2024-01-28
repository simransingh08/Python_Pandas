# creating a density plot using Seaborn

import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data for demonstration
data = sns.load_dataset("iris")

# Create a density plot
plt.figure(figsize=(8, 6))
sns.kdeplot(data['sepal_length'], shade=True, color="b", label="Sepal Length")
sns.kdeplot(data['sepal_width'], shade=True, color="r", label="Sepal Width")

# Add labels and title
plt.xlabel('Length/Width')
plt.ylabel('Density')
plt.title('Density Plot Example')

# Add a legend
plt.legend()

# Display the plot
plt.show()
