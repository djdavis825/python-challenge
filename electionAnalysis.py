"""
Analyze the votes and calculate each of the following values:

1. The total number of votes cast

2. A complete list of candidates who received votes

3. The percentage of votes each candidate won

4. The total number of votes each candidate won

5. The winner of the election based on popular vote
----------------------------
Election Results

Total Votes: 369711

Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)

Winner: Diana DeGette
----------------------------
Your final script should both print the analysis to the terminal and export a text file with the results
"""
import csv
import os

election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

outputFile = os.path.join("electionAnalysis.txt")

# Variables
totalVotes = 0
candidates = [] # empty list
candidateVotes = {} # empty dictionary
win = 0 # win vote count
winCandidate = "" # win candidate

# resd the csv file
with open(election_csv) as electionData:
    csv_reader = csv.reader(electionData, delimiter=",")

    # read header
    header = next(csv_reader)

    # rows are lists
        # index 0 = ballot id
        # index 1 = county
        # index 2 = candidate

    for row in csv_reader:
        # count of total votes
        totalVotes += 1

        if row[2] not in candidates:
            # add to list of candidates
            candidates.append(row[2])

            # add value to dictionary
            candidateVotes[row[2]] = 1

        else:
            # candidate is in list and vote to candidate
            candidateVotes[row[2]] += 1

voteOutput = ""

for candidates in candidateVotes:
    # get vote count and % of votes
    votes = candidateVotes.get(candidates)
    percentage = (float(votes) / float(totalVotes)) * 100.00
    voteOutput += f"{candidates}: {percentage:.2f}% ({votes:,})\n"

    # compare votes to win count
    if votes > win:
        # update to be the new win count
        win = votes
        # update win candidate
        winCandidate = candidates

winCandidateOutput = f"Winner: {winCandidate}\n"

# output
output = (
    f"Election Results \n"
    f"----------------------------\n"
    f"Total Votes = {totalVotes:,}\n"
    f"----------------------------\n"
    f"{voteOutput}"
    f"----------------------------\n"
    f"{winCandidateOutput}"
)

print(output)

# export output to txt file
with open(outputFile, "w") as textFile:
    textFile.write(output)