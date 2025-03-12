import matplotlib.pyplot as plt

# Data for the bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

# Creating the bar chart
plt.bar(categories, values, color='blue')

# Adding labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Simple Bar Chart using Matplotlib")

# Show the plot
plt.show()
