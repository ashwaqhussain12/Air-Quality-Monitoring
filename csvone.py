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
"""

#printing tuple by tuple
for rowln in rows:
	print(" ".join(map(str, rowln)))

