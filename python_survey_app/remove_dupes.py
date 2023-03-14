#TICKET 2 - REMOVE DUPLICATE ENTRIES

import csv

csvfile = 'results.csv' #creating a variable for the csv file

with open(csvfile) as file: #opening the csv file using 'with open'
     reader = csv.reader(file) #reading the csv file using 'reader' function
     csv_data = list(reader) #defining csv_data variable which reads csv columns into a list


def dedupe(csv_data): #defining function
    deduped_data = [] #creating an empty array for the data
    seen_in_csv = set() #set for fast O(1) amortized lookup - https://stackoverflow.com/questions/15741564/how-to-remove-duplicates-from-a-csv-file (amortized = to write off). set() can't contain duplicates.
    for row in csv_data: #looping through each row in the list
        if row[0] not in seen_in_csv: #if row 0 (user ID) is not in the data, append to deduped data
            seen_in_csv.add(row[0]) #using the set() function
            deduped_data.append(row)
    return deduped_data

#QUESTION - HOW DOES THIS IGNORE/REMOVE DUPLICATES???

cleaned_data = dedupe(csv_data)

print(cleaned_data) #print the data to check above code works