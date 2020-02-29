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
for subln in sublst:
	print(" ".join(map(str, subln)))

# Printing the length of list after Deleting NA values
totdatar=len(sublst)
print("Total no. of Rows After Deleting NA values: %d"%(totdatar))
