# Python Homework - PyBank
# Submitted by : Sheetal Bongale
# Python 3.7.4
# This Python script analyzes the monthly financial records

import os
import csv

date = []
total_months = 0
profit_loss = []
change = []

# Open and read budget_data.csv file:
with open(os.path.join('Resources','budget_data.csv'),'r') as in_file:
    budget_data = csv.reader(in_file)
    header = next(budget_data)
    for row in budget_data:
        date.append(row[0])
        profit_loss.append(int(row[1]))
        
# Calculations to analyze the financial data:
total_months = len(date)
net_amount = sum(profit_loss)

for i in range(len(date)-1):
    change.append(profit_loss[i+1] - profit_loss[i])   

avg_change = round(sum(change)/len(change),2) 
max_change = max(change)
max_date = date[change.index(max_change)+1]
min_change = min(change)
min_date = date[change.index(min_change)+1]

# Output Print:
dash_break = "-------------------------------------------------"
print_lines = (
    dash_break +'\n' + "Financial Analysis" +'\n' + dash_break +'\n'
    "Total Months: "+ str(total_months) +'\n'
    "Total: $"+ str(net_amount) +'\n'
    "Average Change: $"+ str(avg_change) +'\n'
    "Greatest Increase in Profits: "+ str(max_date) + " ($" + str(max_change) + ")"'\n'
    "Greatest Decrease in Losses: "+ str(min_date) + " ($" + str(min_change) + ")"'\n' + dash_break +'\n'
    )
print (print_lines)






