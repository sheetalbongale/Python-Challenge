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

#Open election_data.csv file
with open(os.path.join('Resources','election_data.csv'),'r') as in_file:
    election_data = csv.reader(in_file)
    header = next(election_data)
    #Calculate the votes
    for row in election_data:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates:
            candidate_votes[candidates.index(candidate)] += 1
        else:
            candidates.append(candidate)
            candidate_votes.append(1)

print ("total votes: " + str(total_votes))
for count in range(len(candidates)):
        print(f"{candidates[count]}: ({candidate_votes[count]})")

# Calculate the voting percentage for each candidate

# Identify the Election winner

# Print the Election results

# Export the Election analysis text file