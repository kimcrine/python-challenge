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

        #Calculate net profit/loss for period
        current_profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + current_profit_loss

        if (count == 1):
            #Set value of last month equal to current month
            initial_profit_loss = current_profit_loss
            
            continue

        else:

            #Calculate profit/loss change
            delta_profit_loss = current_profit_loss - initial_profit_loss

            #Add each month to the months list
            months.append(row[0])

            #Add each profit loss change calculation to profit/loss changes list
            profit_loss_changes.append(delta_profit_loss)

            #Set last month equal to current month
            initial_profit_loss = current_profit_loss

#Sum and average profit/loss changes
profit_loss_sum = sum(profit_loss_changes)
profit_loss_avg = round(profit_loss_sum/(count - 1),2)

#Greatest increase/decrease (amount)
greatest_profit_incr = max(profit_loss_changes)
greatest_profit_decr = min(profit_loss_changes)

#Greatest increase/decrease (date)
date_incr = profit_loss_changes.index(greatest_profit_incr)
date_decr = profit_loss_changes.index(greatest_profit_decr)

#Identify best and worst months
best_month = months[date_incr]
worst_month = months[date_decr]

#Print analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count}") 
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${profit_loss_avg}")
print(f"Greatest Increase in Profits: {best_month} (${greatest_profit_incr})")
print(f"Greatest Decrease in Profits: {worst_month} (${greatest_profit_decr})")

#Export text file 
pybank_output = os.path.join(".", "Analysis", "analysis.txt")
with open(pybank_output, "w") as txt:
    txt.write("Financial Analysis\n")
    txt.write("----------------------------\n")
    txt.write(f"Total Months: {count}\n")
    txt.write(f"Total: ${net_profit_loss}\n")
    txt.write(f"Average Change: ${profit_loss_avg}\n")
    txt.write(f"Greatest Increase in Profits: {best_month} (${greatest_profit_incr})\n")
    txt.write(f"Greatest Decrease in Profits: {worst_month} (${greatest_profit_decr})\n")