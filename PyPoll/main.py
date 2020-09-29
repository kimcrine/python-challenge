#Import modules
import os
import csv

#Establish path for CSV file
pypoll_csv = os.path.join(".", "Resources", "election_data.csv")

#Create lists to store data
candidates = []
votes_per_candidate = []

#Open and read CSV
with open(pypoll_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)