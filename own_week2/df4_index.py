import pandas as pd

# SETTING UP
dataset_directory = '../resources/week-2/datasets/'
df = pd.read_csv(dataset_directory + 'Admission_Predict.csv', index_col=0)

# CHANGE INDEX - COPY INDEX TO COLUMN
df['Serial Number'] = df.index
df = df.set_index('Chance of Admit ')

# CHANGE INDEX - RESET INDEX BACK TO COLUMN
df = df.reset_index()



# SETTING UP
df = pd.read_csv(dataset_directory + 'census.csv')
df['SUMLEV'].unique()
df = df[df['SUMLEV']==50]
columns_to_keep = ['STNAME', 'CTYNAME', 'BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013', 'BIRTHS2014', 'BIRTHS2015', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
df = df[columns_to_keep]

# MULTILEVEL INDEX
df = df.set_index(['STNAME', 'CTYNAME'])
df.loc[[('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County')]]