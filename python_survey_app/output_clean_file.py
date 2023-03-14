#TICKET 6 - OUTPUT THE CLEANSED RESULT DATA TO A NEW FILE

#importing all of my functions
from remove_dupes import dedupe
from remove_empty import remove_empty_rows
from capital_names import cap_names
from answer3_valid import validate_answer_3

import csv
csvfile = 'results.csv' #creating a variable for the csv file
with open(csvfile) as file: #opening the csv file using 'with open'
    reader = csv.reader(file) #reading the csv file using 'reader' function
    csv_data = list(reader) #defining csv_data variable which reads csv columns into a list


def cleansed_file(csv_data): #defining function
    with open('cleansed_results.csv', 'w', newline='') as csvfile: #creating a new blank csv file and making it writable. Newline ensures each row written to the new file is seperated by a newline character
        writer = csv.writer(csvfile,delimiter=',') #writing to the file using the writer function
        writer.writerows(csv_data) #writing new rows in the file using data from the original csv file, with cleansing actions performed - https://thehelloworldprogram.com/python/python-string-methods/#:~:text=Performing%20the%20.,of%20the%20characters%20to%20lowercase

#calling on all of my functions and then outputting to the cleansed csv
clean_final_data = dedupe(csv_data)
clean_final_data = remove_empty_rows(clean_final_data)
cap_names(clean_final_data)
clean_final_data = validate_answer_3(clean_final_data)
cleansed_file(clean_final_data)


