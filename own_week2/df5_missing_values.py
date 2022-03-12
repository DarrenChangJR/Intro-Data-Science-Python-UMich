import pandas as pd

'''
Missing at Random - omission of answer
Missing Completely at Random - MaR with no correlation to other fields
'''

dataset_directory = '../resources/week-2/datasets/'
df = pd.read_csv(dataset_directory + 'class_grades.csv')

# ISNULL
mask = df.isnull()

# DROPNA
df.dropna(inplace=True)

# FILLNA
df.fillna(0, inplace=True)


df = pd.read_csv(dataset_directory + 'log.csv')
df.reset_index(inplace=True)
df.set_index(['user', 'time'], inplace=True)
df.sort_index(inplace=True)

df = df.fillna(method='ffill')
df.replace('.*.html$', 'webpage', regex=True)

# CUSTOMISED FILL
df = pd.DataFrame({'A': [1,1,2,3,4], 'B': [3,6,3,8,9], 'C': ['a','b','c','d','e']})
df = df.replace([1,3], [100,300])