#Treyton Krupp
#CS3910

import csv
current_dolla = []								#Long data of first table. Format: [[row1], [row2],...]
old_dolla = []									#For 2nd table. Both will be iterated over when read in to

with open('PythonCSV.csv', 'rb') as csvfile:
	overall = csv.reader(csvfile, delimiter=',')	#Read entire csv file into a 2d list
	count = 0									#Count variable to keep track of what row while it iterates through the overal list
	years = []
	
	for row in overall:							#Systematically going through each row of our data		
		if count == 4:							#This first conditional and loop extracts the years(column headers) in to a list. It is the 5th row down in the csv file.
			for n in range(1, len(row), 2):		#The year is every other column. The for loop runs and captures each year in a list 
				years.append(row[n])

		'''State", "Year", "Money Type", "Median Income", "Standard Error'''   #How the columns will be layed out in long format

		if 6 <= count <= 57 :					#Abstract 1st table
			state = row[0]						#Create new rows that will have the following format: "State", "Year", "Money Type", "Median Income", "Standard Error"
			new_row = [state]					#Each "new_row" created will be the new row in the long data
			year_count = 0						#The counter used to cycle through the years grabbed earlier and listed
			for n in range(1,len(row)):			#We start at column 1 and not 0 because we already got the state name
				add = None
				if n % 2 == 1:					#Depending on our count of odd or even we know if we are grabbing median income or standard error
					new_row.append(years[year_count])	#add year. 
					new_row.append("Current")			#since we are in the current table, all Money Types will be current
					add = row[n]	#Median Income
					new_row.append(add)
				if n % 2 == 0:	
					add = row[n]	#Standard Error
					new_row.append(add)
					year_count = year_count + 1			#Each time we end our new row after standard error.
					current_dolla.append(new_row)		#add this new row as a list to a greater list of all the current dollars data
					new_row = [state]					#Then we will have to reset our new row as we will continue to the next row

		if 61 <= count <= 113 :						#Same exact process but for the 2016 dollars
			state = row[0]
			new_row = [state]
			year_count = 0
			for n in range(1,len(row)):
				add = None
				if n % 2 == 1:
					new_row.append(years[year_count])
					new_row.append("2016")
					add = row[n]	#Median Income
					new_row.append(add)
				if n % 2 == 0:	
					add = row[n]	#Standard Error
					new_row.append(add)
					year_count = year_count + 1
					old_dolla.append(new_row)
					new_row = [state]

		count = count +1

headers = ["State", "Year", "Money Type", "Median Income", "Standard Error"]




with open("CleanedData.csv", "wb") as f:		#Create output for long data
	writer = csv.writer(f, delimiter=',')		#Create writer
	writer.writerow(headers)					#Add headers
	for n in range(len(current_dolla)):			#Iterate through the two long data extracted tables. Write every other.
		writer.writerow(current_dolla[n])
		writer.writerow(old_dolla[n])
		

