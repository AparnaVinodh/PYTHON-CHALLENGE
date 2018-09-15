import csv
import os

monthnumber = 0
revenuetotal = 0
presentmonthrev = 0
pastmonthrev = 0
revenuechange = 0
revchanges = []
months = []

filepath = os.path.join("Resources","budget_data.csv")

with open(filepath,'r', newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")

  header=next(csvreader)

  for row in csvreader:
     monthnumber = monthnumber + 1
     months.append(row[0])
     presentmonthrev = int(row[1])
     revenuetotal = revenuetotal + presentmonthrev

     if monthnumber > 1:
         revenuechange = presentmonthrev - pastmonthrev
         revchanges.append(revenuechange)

     pastmonthrev = presentmonthrev


sumofrevchanges = sum(revchanges)
averagechange = sumofrevchanges / (monthnumber - 1)
maxichange = max(revchanges)
minichange = min(revchanges)
maximonthindex = revchanges.index(maxichange)
minimonthindex = revchanges.index(minichange)
maximonth = months[maximonthindex]
minimonth = months[minimonthindex]

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {monthnumber}")
print(f"Total Revenue: ${revenuetotal}")
print(f"Average Revenue Change: ${averagechange}")
print(f"Greatest Increase in Revenue: {maximonth} (${maxichange})")
print(f"Greatest Decrease in Revenue: {minimonth} (${minichange})")

with open("PyBanknote.txt","w") as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write("-------------------------------------------- \n")
    txtfile.write("Total Months: " + str(monthnumber) + "\n")
    txtfile.write("Total Revenue: $" + str(revenuetotal) + "\n")
    txtfile.write("Average Revenue Change: $" + str(averagechange) + "\n")
    txtfile.write("Greatest Decrease in Revenue: " + minimonth + " ($" + str(minichange) + ")" + "\n")
