#TICKET 7 - CREATE AN OUTPUT SCRIPT THAT READS IN THE CSV FILE AND OUTPUTS THE RESULTS TO THE COMMAND LINE
import csv

clean_csv_data = [] #creating an empty array to read the data in from the csv and store
cleancsvfile = 'cleansed_results.csv' #creating a variable for the csv file

with open(cleancsvfile) as file: #opening the csv file using 'with open'
    headers = ['user_id','first_name','last_name','answer_1','answer_2','answer_3'] #adding headers to the output
    reader = csv.reader(file) #reading the csv file using 'reader' function
    for row in reader: #looping through each row of the csv file and appending each row to the array created above
        clean_csv_data.append(row)

from tabulate import tabulate #importing the tabulate module to output the list as a table https://pypi.org/project/tabulate/
print(tabulate(clean_csv_data, headers=headers)) #print the output to the command line with the added headers


