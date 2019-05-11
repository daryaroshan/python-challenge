#Modules
import os
import csv

#Set the path for the CSV file
budget_data = os.path.join("budget_data.csv")

#Variables
totalMonths = 0
total = 0.0
value = 0.0
change = 0
dates = []
profits = []

#reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
   
    #Header row
    csv_header = next(csvreader)

    #First row
    first_row = next(csvreader)
    totalMonths += 1
    total += int(first_row[1])
    value = int(first_row[1])
    
    #Looping each row 
    for row in csvreader:
        
        dates.append(row[0])
        
        # Calculate the change
        change = int(row[1])-value
        profits.append(change)
        #Add to the row
        value = int(row[1])
        
        #Total  months
        totalMonths += 1
        total = total + int(row[1])

    #Greatest increase 
    GreatestIncrease = max(profits)
    GreatestIndex = profits.index(GreatestIncrease)
    GreatestDate = dates[GreatestIndex]

    #Greatest decrease 
    GreatestDecrease = min(profits)
    WorstIndex = profits.index(GreatestDecrease)
    WorstDate = dates[WorstIndex]

    #Average change 
    AvgChange = sum(profits)/len(profits)
    

#Print results 
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(total)}")
print(f"Average Change: ${str(round(AvgChange,2))}")
print(f"Greatest Increase in Profits: {GreatestDate} (${str(GreatestIncrease)})")
print(f"Greatest Decrease in Profits: {WorstDate} (${str(GreatestDecrease)})")
print("---------------------")

# Export text file with the results
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(totalMonths)}")
line4 = str(f"Total: ${str(total)}")
line5 = str(f"Average Change: ${str(round(AvgChange,2))}")
line6 = str(f"Greatest Increase in Profits: {GreatestDate} (${str(GreatestIncrease)})")
line7 = str(f"Greatest Decrease in Profits: {WorstDate} (${str(GreatestDecrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))