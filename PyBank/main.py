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

    #Read through each row of data
    for row in csv_reader:
        #Count months
        count = count + 1

        #Calculate net profit loss for period
        current_profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + current_profit_loss

        if (count == 1):
            #Set value of last month equal to current month
            initial_profit_loss = current_profit_loss
            
            continue

        else:

            #Calculate profit loss change
            delta_profit_loss = current_profit_loss - initial_profit_loss

            #Add each month to the months list
            months.append(row[0])

            #Add each profit loss change calculation to profit loss changes list
            profit_loss_changes.append(delta_profit_loss)

            #Set last month equal to current month
            initial_profit_loss = current_profit_loss


