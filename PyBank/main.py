import os
import csv

pybank_csv = os.path.join("Desktop", "Bootcamp Work", "Homework 3", "python-challenge", "PyBank", "Resources", "budget_data.csv")

with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")