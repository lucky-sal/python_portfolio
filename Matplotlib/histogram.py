from matplotlib import pyplot as plt
import pandas as pd

hist_data = pd.read_csv('lobster_dist.csv')

plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

print(hist_data.head())

plt.hist(hist_data.carapace_length,
         bins=10,
         )

plt.show()

plt.hist(hist_data.carapace_length,
         bins=20,
         )

plt.title("Lobsters tagged by size")
plt.xlabel('Carapace length (mm)')
plt.ylabel('Number tagged')

plt.show()

plt.hist(hist_data.carapace_length,
         bins=30, range=(75, 155), color='gold'
         )

plt.title("Lobsters tagged by size")
plt.xlabel('Carapace length (mm)')
plt.ylabel('Number tagged')
plt.show()