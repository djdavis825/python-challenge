"""
Analyze the records to calculate each of the following values:

1. The total number of months included in the dataset

2. The net total amount of "Profit/Losses" over the entire period

3. The changes in "Profit/Losses" over the entire period, and then the average of those changes

4. The greatest increase in profits (date and amount) over the entire period

5. The greatest decrease in profits (date and amount) over the entire period
----------------------------
Financial Analysis

Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
----------------------------
Your final script should both print the analysis to the terminal and export a text file with the results
"""
import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#Create output file
outputFile = os.path.join("budgetAnalysis.txt")

#Variables
totalMonth = 0
total = 0
changes = []
months = []

with open(budget_csv) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")

    #READ HEADER
    header = next(budget_data)
    firstRow = next(csv_reader)

    #Previous profit
    lastProfit = float(firstRow[1])

    totalMonth += 1 #Count of months
    total += float(firstRow[1])

    for row in csv_reader:
        totalMonth += 1 #Count of months
        total += float(row[1]) #Format and add on to total profit

        netChange = float(row[1]) - lastProfit
        changes.append(netChange) #Add on changes list

        months.append(row[0]) #First month change occurred

        lastProfit = float(row[1])

avgChange = sum(changes) / len(changes)

greatIncrease = [[months,0], changes[0]]
greatDecrease = [[months,0], changes[0]]

for m in range(len(changes)):
    if(changes[m] > greatIncrease[1]):
        greatIncrease[1] = changes[m] #Becomes greatest increase
        greatIncrease[0] = months[m] #Update month

    if(changes[m] < greatDecrease[1]):
        greatDecrease[1] = changes[m] #Becomes greatest decrease
        greatDecrease[0] = months[m] #Update month

#Output
output = (
    f"Financial Analysis \n"
    f"----------------------------\n"
    f"Total Months: {totalMonth} \n"
    f"Total: ${total:,.2f} \n"
    f"Average Change: ${avgChange:,.2f} \n"
    f"Greatest Increase in Profits: {greatIncrease[0]} (${greatIncrease[1]:,.2f}) \n"
    f"Greatest Decrease in Profits: {greatDecrease[0]} (${greatDecrease[1]:,.2f})"

    )

print(output)

with open(outputFile, "w") as textFile:
    textFile.write(output)