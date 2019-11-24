# Python Homework - PyBank
# Submitted by : Sheetal Bongale
# Python 3.7.4
# This Python script analyzes the financial records over a set period

import os
import csv

Date = []
total_months = 0
total_amount = []

# Open budget_data.csv file:
with open(os.path.join('Resources','budget_data.csv'),'r') as in_file:
    budget_data = csv.reader(in_file)
    header = next(budget_data)
    # Find the total months:
    for row in budget_data:
        total_months += 1


