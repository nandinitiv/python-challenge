import os
import csv

election_data=os.path.join("Resources","election_data.csv")

#Count total votes
total_votes=0
    
#Winning candidate and winning count tracker
winning_candidate=""
winning_count=0

#Declare variables
candidate_options = [] #list
candidate_votes = {} #dictionary

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes=total_votes+1

        #candidate names
        cand_name=row[2]

        # Add candidate name to candidate_options if not already in list
        if cand_name not in candidate_options:
            candidate_options.append(cand_name)
            candidate_votes[cand_name] = 0

        # Increment candidate's vote count
        candidate_votes[cand_name] += 1
   
    # Print the results
    
#Export into a text file 
election_analysis=os.path.join("analysis", "election_analysis.txt")
with open(election_analysis, 'w') as txtfile:

    #Declare variable for all results    
    output = (f"Election Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes}\n"
                f"-------------------------\n")
                
    txtfile.write(output)
    print(output)
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = votes / total_votes * 100
        output = f"{candidate}: {percent:.3f}% ({votes})\n"
        txtfile.write(output)
        print(output)
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
    print("-------------------------")
    txtfile.write("-------------------------\n")
    
    # Print and write who the winning candidate is 
    winner=(f"Winner: {winning_candidate}\n")
    print(winner)
    txtfile.write(winner)
    
    print("-------------------------")
    txtfile.write("-------------------------\n")
    
    txtfile.close()

