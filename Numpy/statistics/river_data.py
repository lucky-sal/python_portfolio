# First, we'll import the NumPy module, so we can use its statistical calculation functions.
import numpy as np

water_height = np.array([4.01, 4.03, 4.27, 4.29, 4.19,
                         4.15, 4.16, 4.23, 4.29, 4.19,
                         4.00, 4.22, 4.25, 4.19, 4.10,
                         4.14, 4.03, 4.23, 4.08, 14.20,
                         14.03, 11.20, 8.19, 6.18, 4.04,
                         4.08, 4.11, 4.23, 3.99, 4.23])

# Let's use the function `np.mean()`` to find the average water height:
print(f'mean of water height: {np.mean(water_height)}')

# But wait! We should sort our data to see if there could be any measurements to throw our data off,
# or represent a deviation from the mean:
print(np.sort(water_height))

# Looks like that thunderstorm might have impacted the average height! Let's measure the median to see
# if its more representative of the dataset:
print(f'\nmedian: {np.median(water_height)}')

# While the median tells us where half of our data lies, let's look at a value closer to the end of the dataset.
# We can use percentiles to use a data points position and get its value:
print(f'75 percentile: {np.percentile(water_height, 75)}')

# So far, we've gotten a good idea about specific values. But what about the spread of our data?
# Let's calculate the standard deviation to understand how similar or how different each data point is:

print(f'standard dev: {np.std(water_height)}')

# Great! Just using a few simple functions we've been able to quickly calculate several important measurements
# and can begin analyzing our dataset.
