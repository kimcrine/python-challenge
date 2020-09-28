#Import modules
import os
import csv

#Establish path for CSV file
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

#Create lists to store data
profit = []
monthly_changes = []
date = []

#Initialize variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")