# Moduless
import os
import csv

# Set and initialize variables
totalMonth = 0
netProfitLosses = 0
previousProfitLost = 0
profitLostChange = []
months = []

# Set path file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV file
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
     # Skip the header row
    next(csvreader)

    #loop to read and calculate total months and net profit and lost
    for row in csvreader:
        totalMonth = totalMonth + 1
        netProfitLosses += int(row[1])

        # calculate profit and lost changes and check if month change to new month
        if totalMonth != 1:
            change = int(row[1]) - previousProfitLost
            profitLostChange.append(change)
            months.append(row[0])

        previousProfitLost = int(row[1])

# Calculate average change
averageChange = round(sum(profitLostChange) / len(profitLostChange), 2)

# greatest increase profits and decrease profits
greatInc = max(profitLostChange)
greatDec = min(profitLostChange)
greatest_increase_month = months[profitLostChange.index(greatInc)]
greatest_decrease_month = months[profitLostChange.index(greatDec)]

# print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonth}")
print(f"Total = ${netProfitLosses}")
print(f"Average change = ${averageChange}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatInc})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatDec})")


# Get the current working directory
current_dir = os.getcwd()

# open file directory analysis folder paty
analysis_dir = os.path.join(current_dir, "analysis")

# write the file to the analysis folder
file_path = os.path.join(analysis_dir, "financial_analysis.txt")

# export to test file
with open(file_path, "w", newline ='') as txtfile:
    
    writer = csv.writer(txtfile)
    
    rows = [
        ["Financial Analysis"],
        ["----------------------------"],
        [f"Total Months: {totalMonth}"],
        [f"Total: ${netProfitLosses}"],
        [f"Average Change: ${averageChange}"],
        [f"Greatest Increase in Profits: {greatest_increase_month} (${greatInc})"],
        [f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatDec})"]
    ]

    writer.writerows(rows)  
    




















