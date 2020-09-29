#Import modules
import os
import csv

#Establish path for CSV file
pypoll_csv = os.path.join(".", "Resources", "election_data.csv")

#Create lists to store data
candidates = []
votes = []
name = []

#Open and read CSV
with open(pypoll_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

     #Read through each row of data
    for row in csv_reader:
         candidates.append(row[2])

    #Count votes per candidate and add to the list
    candidate_count = [[x,candidates.count(x)] for x in set(candidates)]

    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    #Zip lists together
    candidate_zip = zip(name,votes)
    candidate_list = list(candidate_zip)

    #Winner of election based on popular vote
    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]

#Total number of votes cast
total_votes = len(candidates)

#Caculate votes per candidate and percentages
correy_total = candidates.count('Correy')
correy_percent = int(correy_total) / int(total_votes)

o_tooley_total = candidates.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes

li_total = candidates.count('Li')
li_percent = li_total / total_votes

khan_total = candidates.count('Khan')
khan_percent = khan_total / total_votes

#Print results
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')