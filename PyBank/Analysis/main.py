import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    #skip header
    csv_header = next(csvreader)

    #List to hold changes in profit / loss
    net_change_list = []
    greatest = ["", 0]
    least = ["", 999999999999]

    total_months = 0
    total_profit = 0

    first_row = next(csvreader)

    total_months = total_months + 1
    total_profit = total_profit + int(first_row[1]) #start at first row instead of 0

    prev_net = int(first_row[1]) #start at the first row instead of 0

    for row in csvreader:
        change_greatest = int(row[1]) - prev_net
        change_least = int(row[1]) - prev_net

        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        prev_net = int(row[1])

        if net_change > greatest[1]:
            greatest[1] = net_change
            greatest[0] = row[0]

        if net_change < least[1]:
            least[1] = net_change
            least[0] = row[0]
     

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Avergage Change: ${round(sum(net_change_list) / (len(net_change_list)), 2)}")
    print(f"Greatest Increase in Profits:{greatest[0]} ${greatest[1]}")
    print(f"Greatest Decrease in Profits:{least[0]} ${least[1]}")

output_file = os.path.join("PyBank.txt")

with open(output_file, "w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${total_profit}")
    file.write("\n")
    file.write(f"Avergage Change: ${round(sum(net_change_list) / (len(net_change_list)), 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: ${max(net_change_list)}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: ${min(net_change_list)}")

