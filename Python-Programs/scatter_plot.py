# Scatter Plot with Mean and Standard Deviation Visualization
"""
This code generates random data and creates a scatter plot to visualize the data points. 
It also calculates the mean and standard deviation of the data and adds markers for the 
mean and horizontal lines for the standard deviation on the plot. The purpose is to visually 
demonstrate the central tendency and spread of the data using pandas, numpy, and matplotlib.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
num_points = 100
x = np.random.randn(num_points)
y = 2 * x + np.random.randn(num_points)

# Create a DataFrame
data = pd.DataFrame({'X': x, 'Y': y})

# Calculate mean and standard deviation
x_mean = np.mean(x)
y_mean = np.mean(y)
x_std = np.std(x)
y_std = np.std(y)

# Scatter plot
plt.scatter(x, y, label='Data Points')

# Plot mean
plt.scatter(x_mean, y_mean, color='red', marker='x', label='Mean')

# Plot standard deviation
plt.axhline(y_mean + y_std, color='green', linestyle='--', label='Standard Deviation')
plt.axhline(y_mean - y_std, color='green', linestyle='--')

# Set labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show the plot
plt.show()

"""
Here, we started by importing the necessary libraries: pandas, numpy, and matplotlib. 
We set a random seed for reproducibility and generate random data using numpy. Then, we 
created a DataFrame using pandas, where 'X' and 'Y' are the column names and x and y 
are the corresponding arrays. Then we calculated the mean and standard deviation using 
numpy's mean and std functions. After that, we created a scatter plot using matplotlib's 
scatter function to visualize the data points. We also added markers for the mean using 
scatter and horizontal lines for the standard deviation using axhline. Finally, we set 
the labels, add a legend, and displayed the plot using show.
"""
