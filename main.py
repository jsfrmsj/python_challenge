import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

#skip header row
    next(csvreader, None)
#The total number of months included in the data set
    months = list(csvreader)
    total_months = len(months)

#The net total amount of profit/losses over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period



