#TICKET 4 - CAPITALIZE USER NAME FIELDS

import csv

csvfile = 'results.csv' #creating a variable for the csv file

with open(csvfile) as file: #opening the csv file using 'with open'
    reader = csv.reader(file) #reading the csv file using 'reader' function
    csv_data = list(reader) #defining csv_data variable which reads csv columns into a list

def cap_names(csv_data): #defining function
    for row in csv_data: #looping through rows in csv_data
        row[1] = row[1].capitalize() #using array for row 1 (first_name) and using capitalize() to capitalize the string
        row[2] = row[2].capitalize() #using array for row 2 (last_name) and using capitalize() to capitalize the string

cap_names(csv_data)

print(csv_data) #print the data to check above code works