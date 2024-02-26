import pandas as pd
data = pd.read_csv('squirrel_data.csv')

fur_counts = data['Primary Fur Color'].value_counts()

data_dict = {
    'Fur Color': fur_counts.index,
    'Count': fur_counts.values
}

fur_df = pd.DataFrame(data_dict)

fur_df.to_csv('squirrel_count.csv', index=False)

print(fur_df.to_string(index=False))
