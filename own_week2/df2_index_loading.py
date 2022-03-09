import pandas as pd


dataset_directory = '../resources/week-2/datasets/'

# CSV
df = pd.read_csv(dataset_directory + 'Admission_Predict.csv', index_col=0)
df.columns

# STRIP WHITESPACE
df = df.rename(mapper=str.strip, axis='columns')

# rename() + dict
df = df.rename(columns={'SOP': 'Statement of Purpose', 'LOR': 'Letter of Recommendation'})

# columns + list
cols = list(df.columns)
cols = [x.lower() for x in cols]
df.columns = cols