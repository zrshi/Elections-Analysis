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

# Create a list for the counties
counties_list = []

# Declare the empty county dictionary to link county to votes
county_votes = {}

# Best turn out and voters number tracker
winning_count_counties = 0
best_county= ""
winning_turnout = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
  
    # read the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the csv file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

         # Print the candidate name from each row
        candidate_name = row[2]

        # Get the County name from each row 
        county_name = row[1]

        # If the county name does not match any existing county
        if county_name not in counties_list:
            #Add it to the list of counties:
            counties_list.append(county_name)

            #BEGIN TRACKING THE COUNTY'S VOTE COUNT
            county_votes[county_name] = 0
        
        # accumulate vote counts for each county
        county_votes[county_name] +=1

        # If the candidate does not match any exisitng candidate...
        if candidate_name not in candidate_options: 
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
        
            # BEGIN TRACKING THE CANDIDATE'S VOTE COUNT
            candidate_votes[candidate_name] = 0

        # accumulate vote counts for each candidate
        candidate_votes[candidate_name] +=1
    
#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n"
    )

    print(election_results, end="")
    # SAVE THE FINAL VOTE COUNT TO THE TEXT FILE.
    txt_file.write(election_results)

    vote_turnout_header= (f'\nCounty Votes:\n')
    print(vote_turnout_header)
    txt_file.write(vote_turnout_header)
    for county_name in county_votes:
        #2. Retrieve vote counts of a county. 
        voters = county_votes[county_name]
        #3. Calculate the percentage of votes
        turnout = int(voters)/int(total_votes) * 100
        county_results = (f"{county_name}: {turnout:.1f}% ({voters:,})\n")
        print(county_results)
        txt_file.write(county_results)
        # Determine best voter turn out 
        # Determine if the votes is greater than the winning count
        if (voters > winning_count_counties) and (turnout > winning_turnout):
            # If true then set winning_count = votes and winning_percent = 
            # vote_percentage
            winning_count_counties = voters
            winning_turnout = turnout
            # And, set the winning candidate eqaul to the candidate's name
            best_county = county_name  
    # Print the winning candidate's results ot the terminal.     
    best_county_summary = ( 
        f"\n-------------------------\n"
        f"Largest County Turnout: {best_county}\n"
        f"---------------------------\n"
        )
    print(best_county_summary)
        
    # Save the winning candidate's name to the text file
    txt_file.write(best_county_summary)    


    # Determine the percentage of votes for each cnadidate by looping thorugh the counts
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        #2. Retrieve vote count of a candidate. 
        votes = candidate_votes[candidate]
        #3. Calculate the percentage of votes
        vote_percentage = int(votes)/int(total_votes) * 100
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = 
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning candidate eqaul to the candidate's name
            winning_candidate = candidate  
    # Print the winning candidate's results ot the terminal.     
    winning_candidate_summary = ( 
        f"-------------------------\n"
        f"winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winniing Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
        
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)   
        


   





