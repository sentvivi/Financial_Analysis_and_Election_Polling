# Financial_Analysis_and_Election_Polling
The project aims to create Python scripts to analyze financial records in the case of PyBank and moderinze vote-counting processes for elections in the case of PyPoll

For PyBank, givena financial dataset with "Date" and "Profit/Losses" columns, and the script is calculate various financial metrics.
  * Calculate the total number of months in the dataset
  * Compute the net total amount of 'Profit/Losses' over the entire period
  * Determine changes in 'Profit/Losses' and calculate the average change
  * Identify the greatest increase in profits (date and amount) and the greatest decrease in profits
  * Generate a report with the analysis results
PyBank script, simply run 'python main.py' in the PyBank directory. The script will read the 'budget_data.csv' file and generate an analysis report in a text file.

 For PyPoll, provided with poll data containing "Voter ID", "County", and "Candidate" columns, and the script will perform vote analysis
  *  Calculate the total number of votes cast
  *  Compile a list of candidates who received vote
  *  Determine the percentage of votes each candidate won
  *  Declare the winner of the election based on popular vote
  *  Produce a report summarizing the election results
For PyPoll, execute 'python main.py' in the PyPoll directory. The script will analyze 'election_data.csv' and output election results

These Python scripts provide valuable insights and analysis for financial data and election results, making them efficient tools for financial reporting and modernizing the vote-counting process.
