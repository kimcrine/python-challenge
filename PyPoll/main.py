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

    #Zip lists together to assign votes per candidate
    candidate_zip = zip(name,votes)
    candidate_list = list(candidate_zip)