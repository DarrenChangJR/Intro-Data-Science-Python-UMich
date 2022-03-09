import pandas as pd

# SETTING UP
dataset_directory = '../resources/week-2/datasets/'
df = pd.read_csv(dataset_directory + 'Admission_Predict.csv', index_col=0)
df.columns = [x.lower().strip() for x in df.columns]
df['cgpa'] *= 0.43

# BOOLEAN MASKING
admit_mask = df['chance of admit'] > 0.7
df.where(admit_mask).dropna()
df[admit_mask]

# FUNCTIONS OF [] - SUMMARY
df['gre score']
df[['gre score', 'cgpa']]
df[df['chance of admit'] > 0.7]

# COMBINE BOOLEAN MASKS
admit_mask = (df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9)
admit_mask = (df['research'] == 1) | (df['cgpa'] >= 3.6)
