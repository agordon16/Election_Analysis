import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    

# Create a filename variable to a direct or indirect path to the file.

  
# Use the open statement to open the file as a text file.

# The data we need to retrieve
# 1.Total number of votes cast
# 2.A complete list of candidates who received votes
# 3.Total number of votes each candidate received
# 4.Percentage of votes each candidate won
# 5.The winner of the election based on popular vote