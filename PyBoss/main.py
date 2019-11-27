# Python Homework - PyBoss
# Submitted by : Sheetal Bongale
# Python 3.8
# This Python script will convert a given dataset to the required format and exports an updated clean .csv file

import os
import csv

# Declaration of empty lists according to required format for parsed data
emp_id = []
first_name = [] 
last_name = []
dob =[]
ssn = []
state = []

# Source: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL',
    'Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
    'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT',
    'Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND',
    'Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD',
    'Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',
}

# Open and read employee_data.csv file:
with open(os.path.join('Resources','employee_data.csv'),'r') as old_file:
    employee_data = csv.DictReader(old_file)
    #next(employee_data)
    # Append the new empty data lists after converting the old data to the new format:
    for row in employee_data:
        
        emp_id.append(row['Emp ID'])
        first_name.append(row['Name'].split(" ")[0])
        last_name.append(row['Name'].split(" ")[1])
        dob.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        ssn.append('***-**-' + row['SSN'].split('-')[2])
        state.append(us_state_abbrev[row['State']])

# Zip the modified entries
clean_csv = zip(emp_id,first_name,last_name,dob,ssn,state)

# Write and Export the new updated csv file:
with open('clean_employee_data.csv' , 'w') as new_file:
    writer = csv.writer(new_file, delimiter = ",")
    writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State']) 
    writer.writerows(clean_csv)
    print ("Updated Employee data file is ready.")