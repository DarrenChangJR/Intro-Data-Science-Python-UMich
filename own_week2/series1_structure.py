import pandas as pd
import numpy as np


# CREATE WITH LIST
students = ['Alice', 'Jack', 'Molly']
pd.Series(students)

numbers = [1,2,3]
pd.Series(numbers)

# None VS NaN
students[-1] = None
pd.Series(students)

numbers[-1] = None
pd.Series(numbers)

np.nan != None
np.isnan(np.nan)

# CREATE WITH DICTIONARY
students[-1] = 'Molly'
students_scores = dict(zip(students, ['Physics', 'Chemistry', 'English']))
s = pd.Series(students_scores)
s.index

# INDEX AND DATA SEPARATELY
pd.Series(['Physics', 'Chemistry', 'English'], index=students)

# MISMATCHED INDEX AND DATA
s = pd.Series(students_scores, index=['Alice', 'Molly', 'Sam'])
print(s)