#TICKET 3 - IGNORE EMPTY LINES

import csv

csvfile = 'results.csv' #creating a variable for the csv file

with open(csvfile) as file: #opening the csv file using 'with open'
    reader = csv.reader(file) #reading the csv file using 'reader' function
    csv_data = list(reader) #defining csv_data variable which reads csv columns into a list


def remove_empty_rows(csv_data): #defining function
    return [row for row in csv_data if any(row)] #looping through rows in csv_data and removing empty rows using if any() - stackoverflow.com/questions/4521426/delete-blank-rows-from-csv

cleaned_data = remove_empty_rows(csv_data) #new variable for the cleaned data

print(cleaned_data) #print the data to check above code works