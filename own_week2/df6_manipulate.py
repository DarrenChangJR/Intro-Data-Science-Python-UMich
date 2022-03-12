import pandas as pd

# SETTING UP
dataset_directory = '../resources/week-2/datasets/'
df = pd.read_csv(dataset_directory + 'presidents.csv', index_col=0)


# .apply()
def splitname(row):
	row['First'] = row['President'].split()[0]
	row['Last'] = row['President'].split()[-1]
	return row

df = df.apply(splitname, axis='columns')

# .str.extract()
pattern = '(?P<First>^[\w]*).* (?P<Last>[\w]*$)'
df['President'].str.extract(pattern)

df['Born'] = df['Born'].str.extract('([\w]{3} [\d]{1,2}, [\d]{4})')
# print(pd.to_datetime(df['Born']))
print(df)