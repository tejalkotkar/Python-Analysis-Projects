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
# create .txt file and open ion append mode

#function to print the output to terminal & .txt file
def print_output(message):

    # Open a .txt file in append mode, as .txt file is not created already this statement will also create a file
    with open(txtfilepath,'a') as txtfile:   

        # Print output to terminal
        print(message)

        # Print oputput message to .txt file
        txtfile.write(message + "\n")

with open(csvpath,'r') as csvfile: 
    # Read from csv file
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Get the csv header , this also skips the header
    csv_header = next(csvreader, None)

    # Initialise toal months variable to 0 and create an empty dictonary
    total_months = 0
    dict_finances = {}

    # Read through all rows and print to dictionary
    for row in csvreader:
        total_months += 1
        dict_finances[row[0]] = int(row[1])

# Calculate Net total amount of "Profit/Losses" over the entire period
Net_profit_loss = sum(dict_finances.values())

# Define an empty dictionary and initialise variable i to 0
average_changes = {}
i = 0

# Iterate through dictonary dict_finances to get the change in profit/loss over a time period
# and add that change to new dictonary called average_changes
for key, value in dict_finances.items():
    # For first iteration just store the key and value 
    if i==0:    
        pre_key = key
        pre_value = value
        i +=1
        continue
    else:           # From second iterations calculate the change in profit/loss and store values for nect calculations
        average_changes[key] = value - pre_value
        pre_key = key
        pre_value = value

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
print_output("Total Monts:" + str(total_months))
print_output("Total: $" + str(Net_profit_loss))
print_output("Average Change: $"+str(Avg_change))
print_output("Greatest Increase in Profits: "+ Max_key + " ($" + str(Max_value) + ")")
print_output("Greatest Increase in Profits: "+ Min_key + " ($" + str(Min_value) + ")")