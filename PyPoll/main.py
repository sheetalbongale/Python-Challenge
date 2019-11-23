# Python Homework - PyPoll
# Submitted by : Sheetal Bongale
# Python 3.7.4
# This Python script analyzes election voting data and identify the election winner

import os
import csv

voter_id = []
county = []
candidates = []
total_votes = 0
candidate_votes = []
vote_percentage = []

#Open election_data.csv file:
with open(os.path.join('Resources','election_data.csv'),'r') as in_file:
    election_data = csv.reader(in_file)
    header = next(election_data)
    #Calculate the votes:
    for row in election_data:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidate_votes[candidates.index(candidate)] += 1
        else:
            candidates.append(candidate)
            candidate_votes.append(1)

# Calculate the voting percentage for each candidate:
for count in range(len(candidates)):
    percentage = round(candidate_votes[count]/total_votes*100,2)
    vote_percentage.append(percentage)

# Identify the Election winner:
election_winner = candidates[candidate_votes.index(max(candidate_votes))]

# Print the Election results:
dash_break = "-------------------------"
print("Election Results")
print(dash_break)
print(f"Total Votes: {total_votes}")
print(dash_break)
for count in range(len(candidates)):
    print(f"{candidates[count]}: {vote_percentage[count]}% ({candidate_votes[count]})")
print(dash_break)
print(f"Winner: {election_winner}")
print(dash_break)

# Export the Election Results text file: