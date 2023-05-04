import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
months = 0
profitslosses = 0
total_change = 0
change_list = []
prev_value = None
month_list = []

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        months += 1
        month_list.append(row[0])
        value = int(row[1])
        profitslosses += value
        
        # Calculate average change by first calculating total change 
        current_value = float(row[1])
        if prev_value is not None:
            change = current_value - prev_value
            change_list.append(change)
        prev_value = current_value

#Export into a text file 
budget_analysis=os.path.join("analysis", "budget_analysis.txt")
with open(budget_analysis, 'w') as txtfile:
    
    output=(f"Financial Analysis\n----------------------------\n")
    print(output)
    txtfile.write(output)
    
    #Print the total months
    total_months = months
    print("Total Months: ", total_months)
    print("Total: $", profitslosses)
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${profitslosses}\n")

    #Calculate and print the average change
    total_change = sum(change_list)
    average_change = total_change / len(change_list)
    print(f"Average Change: ${average_change:.2f}")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")

#Find greatest increase and decrease in profits
#Initialize variables
    max_increase = 0
    max_decrease = 0
    max_increase_month = ''
    max_decrease_month = ''
    for i in range(len(change_list)):
        if change_list[i] > max_increase:
            max_increase = change_list[i]
            max_increase_month = month_list[i+1] # Add 1 to account for first month being skipped
        if change_list[i] < max_decrease:
            max_decrease = change_list[i]
            max_decrease_month = month_list[i+1] # Add 1 to account for first month being skipped

    # Print results
    print(f"Greatest Increase in Profits: {max_increase_month} (${round(max_increase)})")
    txtfile.write(f"Greatest Increase in Profits: {max_increase_month} (${round(max_increase)})\n")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${round(max_decrease)})")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease_month} (${round(max_decrease)})\n")
    
    txtfile.close()