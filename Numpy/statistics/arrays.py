import numpy as np

# temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')
temperatures = np.array([[43.6, 45.1, 58.8, 53.],
                         [47.0, 44.5, 58.3, 52.6],
                         [46.7, 44.2, 57.9, 52.2],
                         [46.5, 44.1, 57.6, 51.9],
                         [46.2, 43.9, 57.2, 51.5]])
print(temperatures)

temperatures_fixed = temperatures + 3

monday_temperatures = temperatures_fixed[0, :]
thursday_friday_morning = temperatures_fixed[3:5, 1]

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) |
                                          (temperatures_fixed > 60)]

print(f'temperatures_fixed = \n{temperatures_fixed}\n'
      f'monday_temperatures = {monday_temperatures}\n'
      f'thursday_friday_morning = {thursday_friday_morning}\n'
      f'temperature_extremes = {temperature_extremes}')