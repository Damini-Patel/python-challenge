# import Modules
import os
import csv

# set path for file
csvpath = os.path.join("..", "PyBank", "Resources\\budget_data.csv")

# open the CSV
with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip header
    csv_header = next(csvfile)

    # set variables
    row_count = 0
    total_pl = 0
    best_amount = 0
    worst_amount = 0
    flag = 1
    average_arr = []

    # read through each line 
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])

        # find the number of rows (months)
        row_count += 1

        # find the total of profit and loss (P/L)
        total_pl += profit_loss

        # find greatest increase and decrease in P/L over entire period
        if flag == 1:
            pl_prev = profit_loss #for next time
            flag = 0
        else:
            pl_current = profit_loss
            difference = pl_current - pl_prev
            pl_prev = profit_loss #For next time

            # find the greatest increase in profit over entire period
            if difference > best_amount:
                best_amount = difference
                best_month = date

            # find the greatest decrease in profit over entire period 
            if difference < worst_amount:
                worst_amount = difference
                worst_month = date

            # find the average change in P/L
            average_arr.append(difference)
    
# print to terminal
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(row_count))
print("Net total amount of Profit/Losses: $ " + str(total_pl))
print("Average Change in Profit/Losses: $" + str("{:.2f}".format(sum(average_arr) / len(average_arr))))
print("Greatest increase in profits: " + best_month + " ($" + str(best_amount) + ")")
print("Greatest dcrease in losses: " + worst_month + " ($" + str(worst_amount) + ")")

# print to text file
with open("PyBank_Results.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("--------------------------------------------\n")
    f.write("Total Months: " + str(row_count) + "\n")
    f.write("Net total amount of Profit/Losses: $ " + str(total_pl) + "\n")
    f.write("Average Change in Profit/Losses: $" + str("{:.2f}".format(sum(average_arr) / len(average_arr))) + "\n")
    f.write("Greatest increase in profits: " + best_month + " ($" + str(best_amount) + ")\n")
    f.write("Greatest dcrease in losses: " + worst_month + " ($" + str(worst_amount) + ")\n")

