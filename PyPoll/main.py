"""
====================== PYTHON CHALLENGE II - PyPoll  ======================
* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.
"""

import os
import csv

# Variable which will hold a csv file path
csvpath = os.path.join('Resources','election_data.csv')

# Variable holding txt file path
txtfilepath = os.path.join('Analysis','VotePoll_Analysis.txt')

#function to print the output to terminal & .txt file
def print_output(message):

    # Open a .txt file in append mode, as .txt file is not created already this statement will also create a file
    with open(txtfilepath,'a') as txtfile:   

        # Print output to terminal
        print(message)

        # Print oputput message to .txt file
        txtfile.write(message + "\n")

# Open CSV file to read from
with open(csvpath,'r') as csvfile: 
    # Read from csv file
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Skip the header
    next(csvreader, None)

    # Initialise toal_votes variable to 0 and create an empty dictonary
    total_votes = 0
    voting = {}

    # Read through all rows and print to dictionary
    for row in csvreader:
        total_votes += 1
        if row[2] not in voting.keys():
            voting[row[2]] = []
        voting[row[2]].append(row[0])

# Print the values to terminal and .txt file
print_output("Election Results")
print_output("----------------------------")
print_output("Total Votes: " + str(total_votes))
print_output("----------------------------")

#Declare an another empty dictonary:
final = {}

# Iterate through each candidate
for key in voting:
    # Get the count of votes for each candidate
    vote_count = len(voting[key])

    # Count the percentage of votes received by candidate
    percent_vote = (vote_count / total_votes) * 100

    # Add key and percent vote to final dictonary
    final[key] = percent_vote

    # Print output to terminal & file
    print_output("{} : {:.3f}% ({})".format(key, percent_vote, vote_count)) 

# Get the candidate with max votes:
winner = max(final, key=final.get)

# Print the result
print_output("----------------------------")
print_output("Winner: {}".format(winner))
print_output("----------------------------")