# 1. Import pandas and matplotlib to get started.

from matplotlib import pyplot as plt
import pandas as pd

# 2. Load in the dataset 2020 monthly avg precipitation around the world - imperial.csv using pandas.
# Check out the first few lines to make sure you know how the data is structured

data = pd.read_csv("2020 monthly avg precipitation around the world - imperial.csv")
print(data.head())

# 3. Write the code to make a line chart with months on the x-axis and Alice Springs precipitation data on
# the y-axis, then print the plot.

plt.plot(data.month_num, data.alice_springs)
plt.show()

# 4. Write the code to add lines to the graph for the other five cities: Windhoek, Quito, Kodiak, Samarqand, and London.
plt.plot(data.month_num, data.alice_springs)
plt.plot(data.month_num, data.windhoek)
plt.plot(data.month_num, data.quito)
plt.plot(data.month_num, data.kodiak)
plt.plot(data.month_num, data.samarqand)
plt.plot(data.month_num, data.london)
plt.show()


# 5. Color the lines in the following groups based on hemisphere:
# Alice Springs (green) and Windhoek (yellowgreen)
# Quito (steelblue)
# Kodiak (chocolate), Samarqand (darkorange) and London (also darkorange)
# (Samarqand and London have the same color because one will have a solid line and the other won’t.)

plt.plot(data.month_num, data.alice_springs, color='green')
plt.plot(data.month_num, data.windhoek, color='yellowgreen')
plt.plot(data.month_num, data.quito, color='steelblue')
plt.plot(data.month_num, data.kodiak, color='chocolate')
plt.plot(data.month_num, data.samarqand, color='darkorange')
plt.plot(data.month_num, data.london, color='darkorange')
plt.show()


# 6. Assign line style to each location based on precipitation type:
# Alice Springs, Windhoek, Quito, and London have rain (solid line)
# Kodiak and Samarqand have rain and snow (dashed or dotted line)
# Choose whichever line style you prefer for Kodiak and Samarqand – just keep it the same for both.
plt.plot(data.month_num, data.alice_springs, color='green', linestyle='solid', label='Alice Springs')
plt.plot(data.month_num, data.windhoek, color='yellowgreen', linestyle='solid', label='Windhoek')
plt.plot(data.month_num, data.quito, color='steelblue', linestyle='solid', label='Quito')
plt.plot(data.month_num, data.kodiak, color='chocolate', linestyle='dashed', label='Kodiak')
plt.plot(data.month_num, data.samarqand, color='darkorange', linestyle='dashed', label='Samarqand')
plt.plot(data.month_num, data.london, color='darkorange', linestyle='solid', label='London')

# plt.show()
# 7. Give the graph an appropriate title.
plt.title('Average Rainfall Around the World, 2020')

# 8. Label the axes “Month” and “Precipitation (in.)”
plt.xlabel('Month')
plt.ylabel('Precipitation (in.)')

# 9. Rotate the tick labels to improve their readability.
plt.tick_params(axis='x', labelrotation=45)

# 10. Create a legend and label the lines that it will show.
plt.legend(bbox_to_anchor=(1, .75))


# plt.show()
# 11. Position the legend by the bottom right-hand corner of the figure, making sure it lies outside the graph and doesn’t block any of the lines from view.



# 12. Use code to export your chart as a .png file.
plt.savefig('research_line_chart.png', dpi=128, bbox_inches='tight')