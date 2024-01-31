from matplotlib import pyplot as plt
import pandas as pd

grammys_data = pd.read_csv('solti_beyonce_grammys.csv')
plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

print(grammys_data.head())

# Make a figure with dimensions of (8,6) and face color of aliceblue. (Add this line of code above the plt.bar() lines.)
fig = plt.figure(figsize=(8, 6), facecolor='aliceblue', tight_layout=True)

# Make sure to run the setup cells to import matplotlib and pandas, display the graphs correctly,
# and load and preview our data. Once you've done that, create two sets of stacked bars using plt.bar():
# Solti's wins and nominations, and Beyoncé's wins and nominations. For each, set the nominations on the bottom.
# Refer back to the grammys_data.head() cell to correctly call each piece of y-data, as well as the years on the x-axis.
# The colors used in the chart are cornflowerblue and orange for Solti, and royalblue and pink for Beyoncé.

plt.bar(x=grammys_data.year, height=grammys_data.solti_nominated, color='cornflowerblue')  # sets bars
plt.bar(x=grammys_data.year, height=grammys_data.solti_won, bottom=grammys_data.solti_nominated,
        color='orange')  # adds in stacked bar
plt.bar(x=grammys_data.year, height=grammys_data.beyonce_nominated, color='royalblue')
plt.bar(x=grammys_data.year, height=grammys_data.beyonce_won, bottom=grammys_data.beyonce_nominated, color='pink')
plt.show()

# Make two subplots, one above and one below. Plot Solti on the top chart and Beyoncé on the bottom chart.

fig = plt.figure(figsize=(8, 6), facecolor='aliceblue', tight_layout=True)
fig.suptitle('Comparing Solti vs Beyonce Grammy Wins/Noms', fontsize=22)
# fig.subplots_adjust(hspace=.5)

plt.subplot(2, 1, 1)
plt.bar(x=grammys_data.year, height=grammys_data.solti_nominated, color='cornflowerblue', label='Nominations')  # sets bars
plt.bar(x=grammys_data.year, height=grammys_data.solti_won, bottom=grammys_data.solti_nominated,
        color='orange', label='Wins')
plt.axvline(x=2000, ymin=0, ymax=1, linewidth=2, color='gray', dashes=(1, 2))
plt.annotate('', (1995, 10), color='black')
plt.annotate(f'Solti: {sum(grammys_data.solti_won)} wins, {sum(grammys_data.solti_nominated)} nominations\n'
             f'from 1963 to 1999.', (2025, 5), fontsize=10, ha='right')
plt.title('Solti')
plt.ylim((0, 11))  # adjust plots axis for each
plt.legend(bbox_to_anchor=(1, 1), frameon=False)  # adds in a legend, labels required in chart

plt.subplot(2, 1, 2)
plt.bar(x=grammys_data.year, height=grammys_data.beyonce_nominated, color='royalblue', label='Nominations')
plt.bar(x=grammys_data.year, height=grammys_data.beyonce_won, bottom=grammys_data.beyonce_nominated, color='pink',
        label='Wins')
plt.axvline(x=1999, ymin=0, ymax=1, linewidth=2, color='gray', dashes=(1, 2))
plt.annotate('', (1996, 10), color='black')
plt.annotate(f'Beyonce: {sum(grammys_data.beyonce_won)} wins, {sum(grammys_data.beyonce_nominated)} nominations\n'
             f'from 2000 to today.', (1961, 5), fontsize=10)
plt.title('Beyonce')
plt.ylim((0, 11))
plt.legend(bbox_to_anchor=(0.2, 1), frameon=False)
plt.savefig('grammy_noms.jpg', dpi=128, bbox_inches='tight')
plt.show()
