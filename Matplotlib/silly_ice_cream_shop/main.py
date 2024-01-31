from matplotlib import pyplot as plt
import pandas as pd

ic_data = pd.read_csv('icecream_data.csv')

plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

print(ic_data.head())

# bar chart
plt.bar(x=ic_data.day, height=ic_data.sales_total, width=0.8, align='center')
plt.errorbar(x=ic_data.day, y=ic_data.sales_total, yerr=ic_data.sales_error, color='orangered', fmt='o')
plt.axhline(y=640, xmin=0, xmax=1, linewidth=2, color='red', dashes=(1, 2))
plt.annotate('Successful day threshold', (20, 600), color='black')
plt.title('Ice Cream Sales in August')
plt.xlabel('Day in August')
plt.ylabel('Sales')
plt.show()

avg_by_day = ic_data.groupby([ic_data['day_of_week_num'], ic_data['day_of_week']])['sales_total'].mean()
avg_by_day = avg_by_day.droplevel(0, 'index').reset_index(name='sales_avg')
print(avg_by_day)

# new bar chart
plt.rcParams['figure.figsize'] = (7, 5)
plt.rcParams['figure.dpi'] = 150

plt.bar(x=avg_by_day.day_of_week, height=avg_by_day.sales_avg, width=0.8, align='center')
plt.axhline(y=640, xmin=0, xmax=1, linewidth=2, color='red', dashes=(1, 2))
plt.annotate('Successful day threshold', (20, 600), color='black')
plt.tick_params(axis='x', labelrotation=45)
# plt.xticks(rotation=-45, ha="left")  # Lets you change the alignment which isnt in tick_params
plt.title('Ice Cream Sales by Day')
plt.xlabel('Day')
plt.ylabel('Sales ($)')
plt.show()

# pie chart
popular_flavors = ic_data.top_flavor.value_counts().rename_axis('flavor').reset_index(name='count')
print(popular_flavors)

plt.pie(x=popular_flavors['count'], labels=popular_flavors['flavor'], colors=['tan', 'saddlebrown', 'lightgreen'])
plt.show()

# scatter
plt.rcParams['figure.figsize'] = (12, 6)

plt.suptitle('Effect of Temperature & Humidity on Ice Cream Sales')

plt.subplot(1, 2, 1)
plt.scatter(x=ic_data.sales_total, y=ic_data.max_temp)
plt.title('Temperature')
plt.ylabel('Temperature (F)')
plt.xlabel('Sales ($)')

plt.subplot(1, 2, 2)
plt.scatter(x=ic_data.sales_total, y=ic_data.humidity_afternoon)
plt.title('Humidity')
plt.ylabel('Humidity (%)')
plt.xlabel('Sales ($)')
plt.show()

# histogram
plt.hist(ic_data.sales_total,
         bins=10,
         )
plt.axvline(x=640, ymin=0, ymax=1, linewidth=2, color='red', dashes=(1, 2))
plt.title('August Sales Total Distribution')
plt.xlabel('Sales Totals')
plt.ylabel('Count of Days')

plt.show()
