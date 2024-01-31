from matplotlib import pyplot as plt
import pandas as pd

hist_data = pd.read_csv('lobster_dist.csv')

plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

plt.hist(hist_data.carapace_length, bins=30, range=(75, 155), color='gold')
plt.axvline(x=83, ymin=0, ymax=1, linewidth=2, color='red', dashes=(1, 2))
plt.axvline(x=127, ymin=0, ymax=1, linewidth=2, color='red', dashes=(1, 2))
plt.annotate('Minimum legal catch size', (84, 23), color='black')
plt.annotate('Maximum legal\ncatch size', (128, 7), color='black')
plt.title('Lobsters tagged by size')
plt.ylabel('Number tagged')
plt.xlabel('Carapace length (mm)')
plt.show()
