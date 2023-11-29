import pandas as pd

filename = 'training_datasets/training_dataset_1.csv'

df = pd.read_csv(filename, encoding='utf-8', low_memory=False)

filtered_df = df.dropna(subset=df.columns[1:]).reset_index(drop=True)

count = len(filtered_df)
print(count)
