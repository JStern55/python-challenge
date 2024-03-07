import os
import csv
from collections import defaultdict


#PyPoll


# Setting the path to the PyPoll CSV file
csv_file_path = os.path.join( 'election_data.csv')
output_file_path = os.path.join('Election_Results.txt')

# Create a defaultdict to store the vote counts for each candidate
candidate_votes = defaultdict(int)

# Read the CSV file
with open (csv_file_path, 'r') as csvfile:
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

