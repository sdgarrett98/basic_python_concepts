# import necessary packages
import csv

# read csv file
election_data = 'Resources/election_data.csv'

# define variables
total_votes = 0
summary = {}
pct_summary = {} # used Xpert
candidate_results = [] # used Xpert

# open the csv file to read from it
with open(election_data, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    # loop through the rows to perform actions on the values
    for row in csvreader:
        # each row in the csv contains a unique month so we can add 1 to the month counter for each row
        total_votes += 1
        # count votes per candidate
        candidate = row[2]

        if candidate in summary:
            summary[candidate] += 1 # used Xpert
        else:
            summary[candidate] = 1 # used Xpert
        
    # calculate percentage of votes for each candidate, used Xpert
    for candidate, votes in summary.items():
        pct = round((votes / total_votes) * 100,3)
        pct_summary[candidate] = pct
    
    # save candidate results to a list
    for candidate, votes in summary.items():
        pct = pct_summary[candidate]
        candidate_result = f'{candidate}: {pct}% ({votes})'
        candidate_results.append(candidate_result)

    # winner
    winner = max(summary, key=summary.get) # used Xpert

    # define variables to be used in terminal and file output
    title = 'Election Results'
    line_break = '-------------------------'
    total_votes_str = f'Total Votes: {total_votes}'
    candidate_1 = f'{candidate_results[0]}' 
    candidate_2 = f'{candidate_results[1]}'
    candidate_3 = f'{candidate_results[2]}'
    winner_str = f'Winner: {winner}'

    print(title)
    print(line_break)
    print(total_votes_str)
    print(line_break)
    print(candidate_1)
    print(candidate_2)
    print(candidate_3)
    print(line_break)
    print(winner_str)
    print(line_break)

    # create a new text file to store the results
    with open('PyPoll/analysis/election_results.txt', 'w') as file:
        lines = '\n'.join([title, line_break, total_votes_str, line_break, candidate_1, candidate_2, candidate_3, line_break, winner_str, line_break]) + '\n' # used Xpert
        file.write(lines)