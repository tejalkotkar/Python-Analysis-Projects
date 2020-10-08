""" BONUS Challange II - PyParagraph
* Import a text file filled with a paragraph of your choosing.

* Assess the passage for each of the following:
  * Approximate word count
  * Approximate sentence count
  * Approximate letter count (per word)
  * Average sentence length (in words)
"""
import re
import os

# Get the file name for paragraph analysis
print("Make sure txt file containing paragraph is saved under directory raw_data.")
filename = input("Enter a file name for paragraph analysis ==> ")

# Contruct filepath
filepath = os.path.join('raw_data',filename)

#function to print the output to terminal & .txt file
def print_output(filename, message):

    # Open a .txt file in append mode, as .txt file is not created already this statement will also create a file
    with open(filename,'a') as txtfile:   

        # Print output to terminal
        print(message)

        # Print oputput message to .txt file
        txtfile.write(message + "\n")

# Open .txt file and read 
with open(filepath, 'r',encoding='utf-8') as f:
    freader = f.readlines()

# Define and initialise variables
word_count = 0
sentence_count = 0
Total_Characters = 0

# Iterate through freader
for paragraph in freader:
    
    # If there is just a empty line (new line) in the file then don't perform any operations on that
    if paragraph != "\n":
        # Approximate word count
        words = [len(word) for word in paragraph.split(" ")]
        word_count = word_count + len(words)
        Total_Characters = Total_Characters + sum(words)

        # Approximate sentence count
        sentences = re.split("(?<=[.!?]) +", paragraph)
        sentence_count = sentence_count + len(sentences)


# Approximate letter count (per word)
AvgLetterCount = round( Total_Characters / word_count, 1)

# Average sentence length (in words)
AvgSenLength = round(word_count/sentence_count, 1)

# Create a analysis file in Analysis Directory
output_file = "Analysis_"+filename

# Contruct filepath
outfilepath = os.path.join('Analysis',output_file)

# Remove/Delete the Analysis file if already exist 
if os.path.exists(outfilepath):
    os.remove(outfilepath)

# Calling a print_output function to print result on terminarl and write to file
print_output(outfilepath, "Paragraph Analysis\n-------------------------")
print_output(outfilepath, "Approximate Word Count : {}".format(word_count))
print_output(outfilepath, "Approximate Sentence Count : {}".format(sentence_count))
print_output(outfilepath, "Approximate Letter Count (per word) : {}".format(AvgLetterCount))
print_output(outfilepath, "Approximate Sentence Length (in words) : {}".format(AvgSenLength))