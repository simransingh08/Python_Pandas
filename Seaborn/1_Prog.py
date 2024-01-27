# creating a scatter plot matrix using Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample iris dataset
iris = sns.load_dataset("iris")

# Create a scatter plot matrix
sns.pairplot(iris, kind="scatter", diag_kind="hist")

# Add title
plt.suptitle('Scatter Plot Matrix')

# Display the plot
plt.show()
