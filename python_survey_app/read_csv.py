#TICKET 1 - READ A CSV FILE

#docs.python.org/3/library/csv/html - reference to website for reading in csv files

import csv #importing the csv module

csv_data = [] #creating an empty array to read the data in from the csv and store
csvfile = 'results.csv' #creating a variable for the csv file

with open(csvfile) as file: #opening the csv file using 'with open'
    reader = csv.reader(file) #reading the csv file using 'reader' function
    for row in reader: #looping through each row of the csv file and appending each row to the array created above
        csv_data.append(row)

print(csv_data) #print the data to check above code works (uncomment)