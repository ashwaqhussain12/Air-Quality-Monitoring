# importing csv module 
import csv 

# csv file name 
filename = "PRSA_data.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile)
	#print(type(csvreader))
	
	# extracting field names through first row 
	fields = next(csvreader) 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	totdata = csvreader.line_num
	print("Total no. of rows: %d"%(totdata)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

"""
# printing first 3 rows 
print('\nAll rows are:\n') 
for row in rows[:3]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') 
print(type(rows))

#printing tuple by tuple
for rowln in rows:
	print(" ".join(map(str, rowln)))
"""                                 

# Deleting tuples with NA Values
sublst = [subl for subl in rows if subl[5] != 'NA']
# print(type(sublst))

"""
# printing first 3 rows after deleting Null Values
print('\nfirst 3 rows are:\n') 
for row in sublst[:3]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n')
"""
#printing tuple by tuple
#for subln in sublst:
	#print(" ".join(map(str, subln)))

# Printing the length of list after Deleting NA values
totdatar=len(sublst)
print("Total no. of Rows After Deleting NA values: %d"%(totdatar))

from pandas import read_csv
from datetime import datetime
import pandas as pd
# load data
def parse(x):
	return datetime.strptime(x, '%Y %m %d %H')
dataset = read_csv('PRSA_data.csv',  parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
dataset.drop('No', axis=1, inplace=True)
# manually specify column names
dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
dataset.index.name = 'date'

"""
print(type(dataset))

with pd.option_context('display.max_rows', None):  # more options can be specified also
    print(dataset)

print(dataset.count(axis=0))

print(dataset.count(axis=1))
"""

# import numpy as np
# import plotly
# import matplotlib.pyplot as plt
# 'exec(%matplotlib inline)'

# import warnings
# warnings.filterwarnings("ignore")

# from fbprophet import Prophet


# temp = dataset[['pollution', 'press']]
# temp.columns = ['ds','y']
# temp.y.plot()
# temp.head()

"""
from matplotlib import pyplot
values = dataset.values
groups = [0, 1, 2, 3, 5, 6, 7]
i = 1
# plot each column
pyplot.figure()
for group in groups:
	pyplot.subplot(len(groups), 1, i)
	pyplot.plot(values[:, group])
	pyplot.title(dataset.columns[group], y=0.5, loc='right')
	i += 1
pyplot.show()

print(dataset.info())

print(dataset.head())

"""

#print(dataset.index)

#print(dataset[dataset.index < '2010-01-02 03:00:00'])

print(dataset[['press']])
