#Import modules
import os
import csv

#Establish path for CSV file
pybank_csv = os.path.join(".", "Resources", "budget_data.csv")

#Create lists to store data
months = []
profit_loss_changes = []

#Initialize variables
count = 0
net_profit_loss = 0
initial_profit_loss = 0
current_profit_loss = 0
delta_profit_loss = 0

#Open and read CSV
with open(pybank_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)



        
