# Import numpy
import numpy as np

# Read from the file.
with open("stats.txt") as f:
    X = f.read().splitlines()
# Print the data set.
print(len(X))

# Convert the values from string to int
for i in range(len(X)):
    X[i] = int(X[i])


mean = np.mean(X)
median = np.median(X)
sd = np.std(X)
variance = np.var(X)

print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", sd)
print("Variance ", variance)

