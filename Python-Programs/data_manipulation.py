# Data Manipulation and Analysis

# Import the required libraries
import numpy as np 
import pandas as pd 

# Creating a numpy array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Creating a pandas DataFrame from the numpy array
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# To Display the DataFrame
print(df)

# For Accessing columns 
column_A = df['A']
print("\nColumn_A \n{}".format(column_A))

# For Accessing rows
row_0 = df.iloc[0]
print("\nRow_0 \n{}".format(row_0))

# Calculating column sum
column_sum = df['B'].sum()
print("\nColumn B sum \n{}".format(column_sum))

# Calculating row mean
row_mean = df.mean(axis=1)
print("\nRow mean \n{}".format(row_mean))

# Filtering rows based on condition
filtered_df = df[df['C'] > 5]
print("\nFiltered DataFrame:")
print(filtered_df)

# Sorting DataFrame by column B in descending order
sorted_df = df.sort_values(by='B', ascending=False)
print("\nSorted DataFrame:")
print(sorted_df)

"""
This notebook is about basic data manipulation and analysis tasks using numpy and 
pandas in Python. The code above explains various operations on a DataFrame, including 
accessing columns and rows, performing calculations(like mean), filtering, and sorting.
"""
