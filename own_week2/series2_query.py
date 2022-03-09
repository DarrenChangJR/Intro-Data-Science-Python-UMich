import pandas as pd
import numpy as np

# INDEX POSITION/LABEL
students_classes = {'Alice': 'Physics', 'Jack': 'Chemistry', 'Molly':'English', 'Sam': 'History'}
s = pd.Series(students_classes)
s.loc['Molly'] == s.iloc[2]

# OPERATIONS (VECTORIZATION)
grades = pd.Series([90, 80, 70, 60])
total = np.sum(grades)
grades /= 2

# ADD DATA
grades.loc['Text'] = 50

# REPEATED INDICES
kelly_classes = pd.Series(['Philosophy', 'Arts', 'Mathematics'], index=['Kelly', 'Kelly', 'Kelly'])
all_classes = s.append(kelly_classes)
all_classes.loc['Kelly']