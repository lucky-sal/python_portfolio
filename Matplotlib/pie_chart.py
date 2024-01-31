from matplotlib import pyplot as plt
import pandas as pd

pie_data = pd.read_csv('EV_market_share.csv')
plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

print(pie_data.head())

plt.pie(x=pie_data.number_sold, labels=pie_data.model, startangle=60)

plt.title('Top 10 EVs sold in the US by count, 2021')
plt.show()
