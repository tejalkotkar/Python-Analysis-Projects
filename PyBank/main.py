"""
====================== PYTHON CHALLENGE I - PyBank  ======================
Task is to create a Python script that analyzes the records to calculate each of the following:
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
"""

import os
import csv

# Variable which will hold a csv file path
csvpath = os.path.join('Resources','budget_data.csv')

# Variable holding txt file path
txtfilepath = os.path.join('Analysis','Financial_Analysis.txt')

# Open csv file to read from 
with open(csvpath,'r') as csvfile: 
    # Read from csv file
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Skipping header
    next(csvreader, None)

    # Initialise variables and create an empty dictonary
    total_months = 0
    pre_value = 0
    Net_profit_loss = 0
    average_changes = {}

    # Read through all rows and print to dictionary
    for row in csvreader:

        # Calculate total number of month
        total_months += 1

        # Calculate Net Profit
        Net_profit_loss = Net_profit_loss + int(row[1])
        
        # Calculating change over months
        # For first iteration when there is no pre data , just store value and from second iteration start calculations
        if pre_value != 0:
           average_changes[row[0]] = int(row[1]) - pre_value

        pre_value = int(row[1])

# Calculating Average change
Avg_change = round(sum(average_changes.values()) / len(average_changes),2)

# Calculating Greatest Increase in profit
Max_key = max(average_changes, key=average_changes.get)
Max_value = max(average_changes.values())

# Calculating Greatest Decrease in profit
Min_key = min(average_changes, key=average_changes.get)
Min_value = min(average_changes.values())

# Concatinate a message in to one string to print
message1 = "Financial Analysis \n---------------------------- \nTotal Monts: {} \nTotal: ${} \nAverage Change {} \n".format(total_months, Net_profit_loss, Avg_change)  
message2 = "Greatest Increase in Profits: {} (${}) \nGreatest Decrease in Profits: {} (${})".format(Max_key, Max_value, Min_key, Min_value)
message = message1 + message2

# Print output to terminal
print(message)

# Open a .txt file in write mode, if .txt file is not created already this statement will create a file as well
with open(txtfilepath,'w') as txtfile: 
    txtfile.write(message)