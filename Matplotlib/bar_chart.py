from matplotlib import pyplot as plt
import pandas as pd

bar_data = pd.read_csv('plant_data_simplified.csv')
plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

print(bar_data.head())

plt.bar(x=bar_data.PH, height=bar_data.average_leaf_width, width=0.8, align='center')
plt.title('Effect of pH on Leaf Width')
plt.xlabel('pH')
plt.ylabel('Leaf Width (cm)')

plt.errorbar(x=bar_data.PH, y=bar_data.average_leaf_width, yerr=bar_data.error, color='orangered', fmt='o')

plt.show()

# Stacked bar method
avg_heights = pd.read_csv('average_heights.csv')
print(avg_heights)

plt.bar(x=avg_heights.family, height=avg_heights.trunk)
plt.bar(x=avg_heights.family, height=avg_heights.leaves, bottom=avg_heights.trunk)
plt.title('Trunk, Crown, and Total Height')
plt.xlabel('Family')
plt.ylabel('Average Height (m)')
plt.tick_params(axis='x', labelrotation=45)
plt.show()
