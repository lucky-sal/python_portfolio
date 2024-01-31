import numpy as np

# calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')
calorie_stats = np.array([70., 120., 70., 50., 110., 110., 110., 130., 90., 90., 120., 110., 120., 110.,
                          110., 110., 100., 110., 110., 110., 100., 110., 100., 100., 110., 110., 100., 120.,
                          120., 110., 100., 110., 100., 110., 120., 120., 110., 110., 110., 140., 110., 100.,
                          110., 100., 150., 150., 160., 100., 120., 140., 90., 130., 120., 100., 50., 50.,
                          100., 100., 120., 100., 90., 110., 110., 80., 90., 90., 110., 110., 90., 110.,
                          140., 100., 110., 110., 100., 100., 110.])
print(calorie_stats)

average_calories = np.mean(calorie_stats)
print(f'\naverage_calories: {round(average_calories, 2)}\n')

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats_sorted)
print(f'\nmedian_calories: {median_calories}')

nth_percentile = np.percentile(calorie_stats, 4)
print(f'\nnth_percentile: {nth_percentile}')

more_calories  = np.mean(calorie_stats > 60)
print(f'cereals with more_calories: {more_calories}')

calorie_std = np.std(calorie_stats)
print(f'calorie_std: {calorie_std}')

#
# Using this analysis you can see the CrunchieMunchie cereal 60 calories per serving is below the average 100 calories of the market.
