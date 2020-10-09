"""
* Import the `employee_data.csv` file, which currently holds employee records like the below:
```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```
* Then convert and export the data to use the following format instead:
```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```
"""

import os
import csv
import datetime

# Variable which will hold a csv file path for file to read from
csvpath = os.path.join('Resources','employee_data.csv')

# Variable holding csv  file path for file to write to
export_csv_path = os.path.join('Exported_CSV','Exported_Employee_Data.csv')

# Remove/Delete the Analysis file if already exist 
if os.path.exists(export_csv_path):
    os.remove(export_csv_path)

# Define a dtictonary for State Abbrevation:
us_state_abbrv = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 
				   'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 
				   'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
				   'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
				   'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
				   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY', }

# Open employee_data.csv file in read mode and Exported_Employee.csv in append mode
with open(csvpath, 'r') as csvfile, open(export_csv_path, 'a', newline='') as exportfile:

    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize csv.writer
    csvwriter = csv.writer(exportfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Skip Header from csvreader
    next(csvreader, None)

    # Iterating through each row
    for row in csvreader:

        # Store emp id in variable
        emp_id = row[0]
        
        # Split name into first name & last name
        name = row[1].split(" ")
        fname = name[0]
        lname = name[1]

        # Change format of DOB
        DOB = datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%d/%Y")

        # Change SSN to hide numbers
        new_SSN = list(row[3])
        count = 0
        for i in range(0,len(new_SSN)):
            if count < 5 and new_SSN[i] != '-':
                new_SSN[i] = '*'
                count += 1
        SSN = ''.join(new_SSN)

        # Use State abbrevations
        for key, value in us_state_abbrv.items():
            if key == row[4]:
                State = value

        # Write to csv file
        csvwriter.writerow([emp_id, fname, lname, DOB, SSN, State])