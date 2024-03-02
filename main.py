import os
import csv
from collections import defaultdict



#PyPoll


# Setting the path to the PyPoll CSV file
csv_file_path = 'C:\\users\\drjus\\python-challenge\\Resources\\election_data.csv'
output_file_path = 'C:\\users\\drjus\\python-challenge\\analysis.txt'

# Create a defaultdict to store the vote counts for each candidate
candidate_votes = defaultdict(int)

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate through each row in the CSV
    for row in reader:
        # Extract data from the row
        candidate = row['Candidate']
        
        # Count the votes for each candidate
        candidate_votes[candidate] += 1

# Calculate total votes
total_votes = sum(candidate_votes.values())

# Write the election results to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Write results for each candidate
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.2f}% ({votes})\n")

    # Find the winner
    winner = max(candidate_votes, key=candidate_votes.get)

    # Write the winner to the text file
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

print(f"Election results have been written to {output_file_path}")

# Set the path to your CSV file
csv_file_path = 'C:\\users\\drjus\\python-challenge\\Resources\\budget_data.csv'
output_file_path = 'C:\\users\\drjus\\python-challenge\\analysis.txt'
# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
monthly_changes = []
months = []


#PyBank


# Reading the PyBank CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate through each row in the CSV
    for row in reader:
        # Extract data from the row
        date = row['Date']
        profit_loss = int(row['Profit/Losses'])
        
        # Calculate total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_loss
        
        # Calculate monthly change
        if total_months > 1:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            months.append(date)
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(monthly_changes) / (total_months - 1)

# Find the greatest increase and decrease in profits
greatest_increase = max(monthly_changes)
greatest_increase_month = months[monthly_changes.index(greatest_increase)]
greatest_decrease = min(monthly_changes)
greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]

# Write the financial analysis to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print(f"Financial analysis results have been written to {output_file_path}")