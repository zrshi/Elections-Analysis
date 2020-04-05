# Add our Dependencies
import csv
import os
import numpy
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resource", "election_results.csv")

# Assign a varaible to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Initialize a Candidate Options list
candidate_options = []

# Declare the empty Candidate dictionary to link name with votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
  
    # read the header row.
    headers = next(file_reader)
    
    # Print each row in the csv file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

         # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any exisitng candidate...
        if candidate_name not in candidate_options: 
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
        
            # BEGIN TRACKING THE CANDIDATE'S VOTE COUNT
            candidate_votes[candidate_name] = 0

        # accumulate vote counts for each candidate
        candidate_votes[candidate_name] +=1
    # Determine the percentage of votes for each cnadidate by looping thorugh the counts
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        #2. Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate]
        #3. Calculate the percentage of votes
        vote_percentage = int(votes)/int(total_votes) * 100
        #4. Print each candidate's name, vote count, and perentage of votes to the terminal
        print(f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = 
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning candidate eqaul to the candidate's name
            winning_candidate = candidate  

    winning_candidate_summary = ( 
        f"-------------------------\n"
        f"winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winniing Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n"
        )

    print(winning_candidate_summary)
    


   





