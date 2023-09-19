# Moduless
import os
import csv

# set and initialize variables
totalVote = 0
candidates = {}
win = ""
winVote = 0

# set path file
csvpath = os.path.join("Resources", "election_data.csv")

# open the CSV file
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
     # skip the header row
    next(csvreader)

    for row in csvreader:
        # calculate the total votes
        totalVote = totalVote + 1

        # calculate votes for each candidate
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

# calculate the percentage of votes each candidate won
candidatePer = {}
for candidate, votes in candidates.items():
    percentage = (votes / totalVote) * 100
    candidatePer[candidate] = round(percentage, 3)

# to find the winner
for candidate, votes in candidates.items():
    if votes > winVote:
        winner = candidate
        winVote = votes

# print the analysis to terminal
print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalVote}")
print("---------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {candidatePer[candidate]}% ({votes})")
print("---------------------------")
print(f"winner: {winner}")
print("---------------------------")

# Get the current working directory
current_dir = os.getcwd()

# open file directory analysis folder paty
analysis_dir = os.path.join(current_dir, "analysis")

# write the file to the analysis folder
file_path = os.path.join(analysis_dir, "election_report.txt")

# export to test file
with open(file_path, "w", newline = '') as txtfile:

    writer = csv.writer(txtfile)

    rows = [
        ["Election Results"],
        ["---------------------------"],
        [f"Total Votes: {totalVote}"],
        ["---------------------------"]
    ]
    
    for candidate, votes in candidates.items():
        candidate_row = [f"{candidate}: {candidatePer[candidate]}% ({votes})"]
        rows.append(candidate_row)

    rows.extend([
        ["---------------------------"],
        [f"winner: {winner}"],
        ["---------------------------"]
         
    ])

    writer.writerows(rows)









