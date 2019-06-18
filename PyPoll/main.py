#Poll Python Code
#import os and CSV
import os, os.path
import csv

poll=os.path.join("..", "PyPoll", "election_data.csv")
poll_length=len(poll)
print(poll_length)

County=[]
Candidate=[]
unique_candidate=[]
candidate_votes=[]
candidate_vote_percent=[]
total_count=0

with open(poll,'r') as csvFile:
    csvReader=csv.reader(csvFile, delimiter=',')
    next(csvReader,None)

    for row in csvReader:
        total_count=total_count+1
        Candidate.append(row[2])
    for x in set(Candidate):
        unique_candidate.append(x)
        count=Candidate.count(x)
        candidate_votes.append(count)
        candidate_vote_percent.append(Candidate.count(x)/total_count)
    Winner=unique_candidate[candidate_votes.index(max(candidate_votes))]
print(Winner)

with open('Election_Results_' + '.txt', 'w') as text:
        text.write("Election Results for file 'election_data" + ".csv'"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Vote: " + str(total_count) + "\n")
        text.write("----------------------------------------------------------\n")
        for i in range(len(set(Candidate))):
            text.write(unique_candidate[i] + ": " + str(round(candidate_vote_percent[i]*100,1)) +"% (" + str(candidate_votes[i]) + ")\n")
        text.write("----------------------------------------------------------\n")
        text.write("Winner: " + Winner +"\n")
        text.write("----------------------------------------------------------\n")
    