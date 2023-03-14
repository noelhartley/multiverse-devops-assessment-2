#TICKET 5 - VALIDATE THE RESPONSES TO ANSWER 3

import csv

csvfile = 'results.csv' #creating a variable for the csv file

with open(csvfile) as file: #opening the csv file using 'with open'
    reader = csv.reader(file) #reading the csv file using 'reader' function
    csv_data = list(reader) #defining csv_data variable which reads csv columns into a list


def validate_answer_3(csv_data): #defining function
    answer3_valid = [] #creating an empty array for the data
    for answer_3 in csv_data: #looping through each row in csv_data
        try:
            answer_3_field = int(answer_3[5]) #answer 3 in cvs_data must have a numeric value between 1 and 10. Any rows with an invalid value are ignored. Using array for row 5 (answer_£)
            if answer_3_field >= 1 and answer_3_field <= 10: #if the answer is greater than or equal to 1, and less than or equal to 10, append to answer3_valid
                answer3_valid.append(answer_3)                                        
        except: 
            pass #else, pass the row
    return answer3_valid

cleaned_data = validate_answer_3(csv_data)

print(cleaned_data) #print the data to check above code works