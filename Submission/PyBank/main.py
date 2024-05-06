# import necessary packages
import csv

# goal: create a python script analyze financial records stored in budget_data.csv

# read csv file
budget_data = 'Resources/budget_data.csv'

# create variables
budget = {}
dates = []
changes = []

total_months = 0
net_total = 0
prev_prof_loss = None # used Xpert

# open the csv file to read from it
with open(budget_data, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    # loop through the rows to perform actions on the values
    for row in csvreader:
        # each row in the csv contains a unique month so we can add 1 to the month counter for each row
        total_months += 1
        # add profit/loss to get net total
        net_total += int(row[1])
        # append dates to the dates list
        date = row[0]
        dates.append(date)
        # Calculate change in profit/losses
        curr_prof_loss = int(row[1])
        if prev_prof_loss is not None:
            change = curr_prof_loss - prev_prof_loss
            changes.append(change)
        prev_prof_loss = curr_prof_loss

    # set dictionary key values to corresponding list creaeted in the loop above
    budget["month"] = dates
    budget["difference"] = changes

    # average change in profits month over month
    avg_change = round(sum(changes) / len(changes),2)
    
    # greates increase in profits
    max_change_index = budget["difference"].index(max(budget["difference"])) # used Xpert
    max_change_index_adj = max_change_index + 1 # used Xpert, need to adjust by one since the difference list compares records which results in fewer records than month
    max_change_month = budget["month"][max_change_index_adj]
    
    # greatest decrease in profits
    min_change_index = budget["difference"].index(min(budget["difference"])) # used Xpert
    min_change_index_adj = min_change_index + 1 # used Xpert, need to adjust by one since the difference list compares records which results in fewer records than month
    min_change_month = budget["month"][min_change_index_adj]

    # write results to variables for use in terminal and file output
    title = 'Financial Analysis'
    line_break = '----------------------------'
    total_month_str = f'Total Months: {total_months}'
    total_str = f'Total: ${net_total}'
    avg_change_str = f'Average Change: ${avg_change}'
    greatest_inc_str = f'Greatest Increase in Profits: {max_change_month} (${max(budget["difference"])})'
    greatest_dec_str = f'Greatest Decrease in Profits: {min_change_month} (${min(budget["difference"])})'

    # print results to terminal
    print(title)
    print(line_break)
    print(total_month_str)
    print(total_str)
    print(avg_change_str)
    print(greatest_inc_str)
    print(greatest_dec_str)

    # create a new text file to store the results
    with open('Pybank/analysis/financial_analysis.txt', 'w') as file:
        lines = '\n'.join([title, line_break, total_month_str, total_str, avg_change_str, greatest_inc_str, greatest_dec_str]) + '\n' # used Xpert
        file.write(lines)
