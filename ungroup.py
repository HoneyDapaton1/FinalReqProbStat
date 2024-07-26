import numpy as np
from statistics import median, mode, StatisticsError
import matplotlib.pyplot as plt

# Step 1: Organize the Data
data = [121.4, 121.4 , 121.1, 120.9, 120.9 , 121.1 , 121.2 , 122.5 , 123.9 , 123.7 , 123.9 , 124.1]

# Step 2: Sort the Data
sorted_data = sorted(data)
print("Sorted Data:", sorted_data)

# Step 3: Calculate Mean, Median, and Mode
mean = np.mean(data)
median = median(data)
try:
    mode_value = mode(data)
except StatisticsError:
    mode_value = "No mode found"

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode_value)

# Step 4: Calculate Variance and Standard Deviation
variance = np.var(data)
std_deviation = np.std(data)

print("Variance:", variance)
print("Standard Deviation:", std_deviation)

# Step 5: Calculate Coefficient of Variation
coefficient_of_variation = (std_deviation / mean) * 100
print("Coefficient of Variation:", coefficient_of_variation)

# Step 6: Plot Histogram
plt.hist(data, bins=10, edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()