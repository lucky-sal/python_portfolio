from matplotlib import pyplot as plt
import pandas as pd

# load dataset
line_data = pd.read_csv('2020-monthly-avg-temps-f.csv')
print(line_data.head())  # .head() prints a 5x5 snapshot of the table as default DataFrame.head(n=5)

# size chart
plt.rcParams['figure.figsize'] = (10, 6)  # resizes graph
plt.rcParams['figure.dpi'] = 75  # dots per inch, pixel sizes

# plot and format line chart
plt.plot(line_data.month_name, line_data.alice_springs_avg_high, color='green', linestyle='dotted', label='Alice Springs')
plt.plot(line_data.month_name, line_data.windhoek_avg_high, color='green', linestyle='dashed', label='Windhoek')
plt.plot(line_data.month_name, line_data.quito_avg_high, color='steelblue', linewidth=2.5, label='Quito')
plt.plot(line_data.month_name, line_data.kodiak_avg_high, color='darkorange', label='Kodiak')
plt.plot(line_data.month_name, line_data.samarqand_avg_high, color='darkorange', linestyle='dashed', label='Samarqand')
plt.plot(line_data.month_name, line_data.london_avg_high, color='darkorange', linestyle='dotted', label='London')

# add additional formatting features
plt.title('Average High Temps Around the World, 2020')
plt.legend(bbox_to_anchor=(1, .75)) # requires label= in plot function above
plt.ylabel("Temperature (F)")
plt.xlabel("Month")
plt.tick_params(axis='x', labelrotation=45)
# plt.tick_params(axis='x', direction='out', color='red', labelsize='large', labelcolor='purple', labelrotation=30)
plt.savefig('line_chart.png', dpi=128, bbox_inches='tight')  # needs to be called before plt.show()
plt.show()
