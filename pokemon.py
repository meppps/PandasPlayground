import pandas as pd

# df = dataframe
df = pd.read_csv('pokemon.csv')

# Read Excel files
# df_xlsx = pd.read_excel('pokemon_data.xlsx')


# Print top or bottom
df.head(3)
df.tail(3)
df.columns

# print(df[['Name', 'Type 1', 'HP']])

# Specific Location
df.iloc[0:4]
df.iloc[2,1]


# for index, row in df.iterrows():
    # print(index,row)

# Sort By Values
df.sort_values('Name', ascending=False)
df.sort_values(['Type 1', 'HP'])


# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]
df['Total']




# export to [file format], remove extra index col
# df.to_csv('modified.csv', index=False)
# df.to_excel('xmodified.xlsx', index=False)
# df.to_csv('modified.txt', index=False, sep='\t')

grass = df.loc[df['Type 1'] == 'Grass']
# print(grass)
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & df['HP'] > 70]


# Get Rows that do or do not contain values
mega = df.loc[df['Name'].str.contains('Mega')]
notMega = mega = df.loc[~df['Name'].str.contains('Mega')]
# print(notMega)

import re
regTrue = df.loc[df['Name'].str.contains('Fire|Grass', regex=True)]
# print(regTrue)






