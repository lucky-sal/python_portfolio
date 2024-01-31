import numpy as np

allergy_trials = np.array([[6, 1, 3, 8, 2],
                           [2, 6, 3, 9, 8],
                           [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)
trial_mean = np.mean(allergy_trials, axis=1)  # 1 = rows 0 = columns # calculates the mean of each row
patient_mean = np.mean(allergy_trials, axis=0)
print(f'total_mean: {total_mean}')
print(f'trial_mean: {trial_mean}')
print(f'patient_mean: {patient_mean}')

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)

interquartile_range = third_quarter - first_quarter

print(f'first_quarter: {first_quarter}')
print(f'third_quarter: {third_quarter}')
print(f'interquartile_range: {interquartile_range}')

movies_std = np.std(movies_watched)
print(f'movies_std: {movies_std} ')

movies_top_scores = np.mean(movies_watched > 7)  # calculates the % of movies that were greater than 7 (1/15)

print(f'movies_top_scores: {movies_top_scores}')