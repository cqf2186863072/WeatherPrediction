import pandas as pd

filename = 'training_datasets/training_dataset.csv'
output_filename = 'training_datasets/training_dataset_1.csv'

df = pd.read_csv(filename, delimiter=',', encoding='gb18030', low_memory=False)

df['WW'].fillna('云量发展情况没有进行观测或无法观测。 ', inplace=True)
df['Nh'].fillna('0', inplace=True)
df['H'].fillna('2500或更高，或无云。', inplace=True)
df['RRR'].fillna('无降水', inplace=True)
df['tR'].fillna('0', inplace=True)

df.to_csv(output_filename, index=False)
