import re
dataset_directory = '../resources/week-1/datasets/'

text = 'This is a good day.'
re.match('This', text)
re.search('good', text)
re.search('^Amy', text) # anchor
re.search('day.$', text) # anchor

# TOKENIZING
text = 'Amy works diligently. Amy gets good grades. Our studennt Amy is successful.'
re.split('Amy', text)
re.findall('Amy', text)

# PATTERNS AND CHARACTER CLASSES
grades = 'ACAAAABCBCBAA'
re.findall('A[B-C]', grades) # set operator
re.findall('AB|BC', grades) # or
re.findall('[^A]', grades) # negate

# QUANTIFIERS
re.findall('A{2,10}', grades)
re.findall('A{2}', grades)
re.findall('A{2,}', grades)
re.findall('A*', grades)
re.findall('A?', grades)
re.findall('A+', grades)

with open(dataset_directory + 'ferpa.txt', 'r') as file:
	wiki = file.read()
	for item in re.finditer('([\w ]*)(\[edit\])', wiki):
		item.groups()
		item.group(1)
	for item in re.finditer('(?P<title>[\w ]*)\[edit\]', wiki):
		item.groupdict()

# LOOK-AHEAD & LOOK-BEHIND
with open(dataset_directory + 'buddhist.txt', 'r', encoding='TIS-620') as file:
	wiki = file.read()
	pattern = '''
	(?P<title>.*) #uni title
	(โ\ located\ in\ ) #position indicator
	(?P<city>\w*)
	(,\ )
	(?P<country>\w*)'''
	for item in re.finditer(pattern, wiki, re.VERBOSE):
		item.groupdict()