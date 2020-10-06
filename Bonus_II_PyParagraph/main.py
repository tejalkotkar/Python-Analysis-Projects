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

message1 = "\nParagraph Analysis\n-------------------------\nApproximate Word Count : {}\nApproximate Sentence Count : {}\n".format(word_count, sentence_count)
message2 = "Approximate Letter Count (per word) : {}\nApproximate Sentence Length (in words) : {}".format(AvgLetterCount, AvgSenLength)
message = message1 + message2

# Print analysis on terminal
print(message)

# Create a analysis file in Analysis Directory
output_file = "Analysis_"+filename

# Contruct filepath
outfilepath = os.path.join('Analysis',output_file)

# Create output file, open it in write mode and print the analysis
with open(outfilepath, 'w') as outfile:
    outfile.write(message)