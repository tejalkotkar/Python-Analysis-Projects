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

# Remove/Delete the Analysis file if already exist 
if os.path.exists(txtfilepath):
    os.remove(txtfilepath)

#function to print the output to terminal & .txt file
def print_output(message):

    # Open a .txt file in append mode, as .txt file is not created already this statement will also create a file
    with open(txtfilepath,'a') as txtfile:   

        # Print output to terminal
        print(message)

        # Print oputput message to .txt file
        txtfile.write(message + "\n")

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

# Print the values to terminal and .txt file
print_output("PyBank Financial Analysis")
print_output("----------------------------")
print_output("Total Monts: {}".format(total_months))
print_output("Total: ${}".format(Net_profit_loss))
print_output("Average Change: ${}".format(Avg_change))
print_output("Greatest Increase in Profits: {} (${})".format(Max_key, Max_value))
print_output("Greatest Increase in Profits: {} (${})".format(Min_key,Min_value))