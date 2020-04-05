import csv
import os
import numpy
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resource", "election_results.csv")

# Assign a varaible to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do : read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)



