import matplotlib.pyplot as plt
import numpy as np

# Print assignment description
print('''---- Assignment 3 - Working with Matplotlib
Objective: Practice data visualization techniques for better data representation.  
Step 2 Create a new Python script matplotlib_assignment.ipynb. Import Matplotlib and follow these steps:  
1. Create a simple line plot for the following data:
  
  x = [1, 2, 3, 4, 5]
  y = [10, 15, 25, 30, 50]
  
  a. Plot the data.  
  b. Customize the plot by adding a title, axis labels, and a grid.  
''')

# Create a 2x2 grid of subplots
plt.figure(figsize=(10, 8))

# --- Plot 1: Line Plot ---
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, first subplot
print("\n---  b. Customize the plot by adding a title, axis labels, and a grid.----")
plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# --- Plot 2: Bar Graph ---
print('''\n2. Create a bar graph to represent the marks scored by students in a subject:  
  
  students = ['John', 'Jane', 'Alice', 'Bob']
  marks = [75, 85, 60, 90]
  
  a. Plot the data as a bar graph.  
  b. Customize the colors and add a title.  
----''')
students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]

plt.subplot(2, 2, 2)  # 2 rows, 2 columns, second subplot
plt.bar(students, marks, color=['red', 'yellow', 'green', 'orange'])
plt.title("Marks Scored by Students")
plt.xlabel("Students")
plt.ylabel("Marks")

# --- Plot 3: Pie Chart ---
print('''\n-----3. Create a pie chart to represent the percentage distribution of a company’s revenue from different regions:  
  
  regions = ['North America', 'Europe', 'Asia', 'Others']
  revenue = [45, 25, 20, 10]
  
  a. Create a pie chart with the region names as labels.  
  b. Highlight the region with the highest revenue.  
 -----''')

# Data for pie chart
regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]
print("\n ---pie chart---")

plt.subplot(2, 2, 3)  # 2 rows, 2 columns, third subplot
plt.pie(revenue, labels=regions, startangle=90, autopct='%1.0f%%')  # Add percentage labels
plt.title("Revenue Distribution by Region")

# Adjust layout to prevent overlap
plt.tight_layout()



print('''\n----- 4. Generate a histogram to show the frequency distribution of randomly generated integers between 1 and 100 (sample size = 1000).  
-----''')
plt.subplot(2,2,4)
# Generate 1000 random integers between 1 and 100
random_data = np.random.randint(1, 101, 1000)

# Create a histogram

plt.hist(random_data, bins=10, edgecolor='black',color='grey')

# Add titles and labels
plt.title('Frequency Distribution of Random Integers (1 to 100)')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()

'''
here in tha last i use plt.show() function to adjust different charts
'''