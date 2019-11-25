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

# Output print format:
dash_break = "-------------------------------------------------"
print_lines = (
    dash_break + "\n" + "Financial Analysis" + "\n" + dash_break +"\n"
    f"Total Months: {total_months} \n"
    f"Total: ${net_amount} \n"
    f"Average Change: ${avg_change} \n"
    f"Greatest Increase in Profits: {max_date} $({max_change}) \n"
    f"Greatest Decrease in Losses: {min_date} $({min_change}) \n" + dash_break +"\n"
    )

# Print & Export the Financial Analysis text file:
analysis_file = open('Financial_analysis.txt','w+')
analysis_file.writelines(print_lines)
analysis_file.close()
analysis_file = open('Financial_analysis.txt','r+')
print(analysis_file.read())