import os
import csv

election_data = os.path.join("..", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

#skip header row
    csv_header = next(csvreader)

#Total number of votes cast

    total_votes = 0

    casper_count = 0
    DeGette_Count = 0
    Doane_Count = 0

    casper_percent = 0
    DeGette_percent = 0
    Doane_percent = 0
   
    for row in csvreader:
        total_votes = total_votes + 1  
    
        if row[2] == "Charles Casper Stockham":
            casper_count = (casper_count + 1)
        elif row[2] == "Diana DeGette":
            DeGette_Count = (DeGette_Count + 1)
        elif row[2] == "Raymon Anthony Doane":
            Doane_Count = (Doane_Count + 1)

casper_percent = round((casper_count / total_votes) *100, 3)
DeGette_percent = round((DeGette_Count / total_votes) *100, 3)
Doane_percent = round((Doane_Count / total_votes) *100, 3)
    
Results = {"Charles Casper Stockham":casper_count,"Diana DeGette":DeGette_Count,"Raymon Anthony Doane":Doane_Count}

print("Election Results")
print("----------------------------------")
print(f"Total votes: {total_votes}")
print("----------------------------------")
print(f"Charles Casper Stockham: {casper_percent}% ({casper_count}) ")
print(f"Diana DeGette: {DeGette_percent}% ({DeGette_Count}) ")
print(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_Count}) ")
print("----------------------------------")
print(f"Winner {max(Results, key = Results.get)}")
print("----------------------------------")

output_file = os.path.join("election_results.txt")

with open(output_file, "w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------------")
    file.write("\n")
    file.write(f"Total votes: {total_votes}")
    file.write("\n")
    file.write("----------------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {casper_percent}% ({casper_count}) ")
    file.write("\n")
    file.write(f"Diana DeGette: {DeGette_percent}% ({DeGette_Count}) ")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_Count}) ")
    file.write("\n")
    file.write("----------------------------------")
    file.write("\n")
    file.write(f"Winner {max(Results, key = Results.get)}")
    file.write("\n")
    file.write("----------------------------------")