import os
import csv

election_data = os.path.join("election_data.csv")

#Lists
candidates = []
VoteNums = []
VotesPercentage = []

TotalVotes = 0

#reading the CSV file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
     #Header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to votes
        TotalVotes += 1 

        # candidate is not list
        if row[2] not in candidates:
            # Add the candidate to list
            candidates.append(row[2])
            index = candidates.index(row[2])
            VoteNums.append(1)
        
        # candidate in list
        else:
            index = candidates.index(row[2])
            VoteNums[index] += 1
    
    #Vote percentage list 
    for votes in VoteNums:
        percentage = (votes/TotalVotes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        VotesPercentage.append(percentage)
    
    #Candidate Winner
    winner = max(VoteNums)
    index = VoteNums.index(winner)
    CandidateWinner = candidates[index]

#Print results 
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(TotalVotes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(VotesPercentage[i])} ({str(VoteNums[i])})")
print("--------------------------")
print(f"Winner: {CandidateWinner}")
print("--------------------------")

# Export text file with the results
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(TotalVotes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(VotesPercentage[i])} ({str(VoteNums[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {CandidateWinner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))