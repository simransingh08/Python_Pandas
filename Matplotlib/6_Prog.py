# creating a pie chart using Matplotlib
import matplotlib.pyplot as plt

# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [25, 30, 20, 25]
colors = ['lightcoral', 'lightblue', 'lightgreen', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # Explode the first slice

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Add a title
plt.title('Pie Chart Example')

# Display the plot
plt.show()
