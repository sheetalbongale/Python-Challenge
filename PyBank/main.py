# Python Homework - PyBank
# Submitted by : Sheetal Bongale
# Python 3.7.4
# This Python script analyzes the financial records over a set period

import os
import csv

date = []
total_months = 0
profit_loss = []
net_amount = []
change = []

# Open and read budget_data.csv file:
with open(os.path.join('Resources','budget_data.csv'),'r') as in_file:
    budget_data = csv.reader(in_file)
    header = next(budget_data)
    for row in budget_data:
        date.append(row[0])
        profit_loss.append(row[1])
        
# Find the total months:
total_months = len(date)
print (str(total_months))

# Calculate net total amount of Profit/losses
profit_loss = [int(row) for row in profit_loss]
net_amount = sum(profit_loss)
print (str(net_amount))






