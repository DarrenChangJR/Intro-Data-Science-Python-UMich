import pandas as pd

records = [{'Name': 'Alice', 'Class': 'Physics', 'Score': 85},
{'Name': 'Jack', 'Class': 'Chemistry', 'Score': 82},
{'Name': 'Helen', 'Class': 'Biology', 'Score': 90}]

df = pd.DataFrame(records, index=['school1', 'school2', 'school1'])

# INDEX 2D
print(df)
'''
iloc and loc for row selection
indexing operator for column selection (always label based)
"column projection"
'''
df.loc['school1']
df['Name']
df.loc['school1', 'Name']

# CHAINING (may create copy instead of view of df)
df['Name'].loc['school2']

# SLICING
df.loc[:,['Name', 'Score']]

# DROP
df.drop('school1')
copy_df = df.copy()
copy_df.drop('Name', axis=1, inplace=True)
del copy_df['Class']

# ADD
df['ClassRanking'] = None
df.loc['school3'] = None
print(df)