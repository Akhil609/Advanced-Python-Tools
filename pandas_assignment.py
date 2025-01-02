import pandas as pd

print('''1. Create a DataFrame with the following data:  

  }
  a. Print the first five rows of the DataFrame.  
  b. Get the summary statistics of the 'Age' and 'Salary' columns.  
  c. Calculate the average salary of employees in the 'HR' department.  


2. Add a new column, 'Bonus', which is 10% of the salary.  


3. Filter the DataFrame to show employees aged between 25 and 30.  


4. Group the data by 'Department' and calculate the average salary for each department.  


5. Sort the DataFrame by 'Salary' in ascending order and save the result to a new CSV file.  
 
''')

# Data dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

# Create DataFrame from the dictionary
df = pd.DataFrame(data)  # Use df instead of df_original

# a. Print the first five rows of the DataFrame
print("\nFirst five rows of the DataFrame:")
print(df.head())  # This will print the first 5 rows of df

# b. Get the summary statistics of the 'Age' and 'Salary' columns
summary_stats = df[['Age', 'Salary']].describe()
print("\nSummary statistics of 'Age' and 'Salary':")
print(summary_stats)

# c. Calculate the average salary of employees in the 'HR' department
avg_salary_hr = df[df['Department']=='HR']['Salary'].mean()
print("\nAverage salary in the 'HR' department:", avg_salary_hr)

# 2. Add a new column 'Bonus', which is 10% of the salary
df['Bonus']=df['Salary']*(0.1)
print("\nDataFrame after adding the 'Bonus' column:")
print(df)

# 3.Filter the DataFrame to show employees aged between 25 and 30
print("\nFilter the DataFrame to show employees aged between 25 and 30")
filtered_df = df[(df['Age']>=25) & (df['Age']<=30)]
print(filtered_df)

# 4. Group the data by 'Department' and calculate the average salary for each department
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print("\nAverage salary by department:")
print(avg_salary_by_dept)

# 5. Sort the DataFrame by 'Salary' in ascending order and save the result to a new CSV file
sorted_df = df.sort_values(by='Salary', ascending=True)
sorted_df.to_csv('sorted_employee_data.csv', index=False)
print("\nData sorted by 'Salary' and saved to 'sorted_employee_data.csv'.")
