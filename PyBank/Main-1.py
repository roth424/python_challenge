#Bank Python Code
#import os and CSV
import os, os.path
import csv


budget=os.path.join("..","PyBank", "budget_data.csv")
budget_length=len(budget)
print(budget_length)


#budget=os.join(cwd, "budget_data.csv")

for numbers in range(budget_length):
 #Set empty list variables
  date = []
  revenue =[]
  month = []
  year =[]
  revenueChange =[]
  TotalRev =0
  TotalRevChange = []
  RevBeg=0
  itemCount = 0

with open(budget,'r') as csvFile:
    csvReader=csv.reader(csvFile, delimiter=',')
    next(csvReader,None)

    for row in csvReader:
      #itemCount=itemCount + 1
      date.append(row[0])
      revenue.append(int(row[1]))
      TotalRev=TotalRev + int(row[1])
      RevEnd=int(row[1])
      revChange=int(RevEnd-RevBeg)
      TotalRevChange.append(revChange)
      #revenueChange.append(revChange)
      splitdate=row[0].split('-')
      year.append(splitdate[1][-2:])
      RevBeg=RevEnd

print(TotalRevChange)
AveRevChg=sum(TotalRevChange)/len(TotalRevChange)
print(AveRevChg)
GIncrease=max(TotalRevChange)
GDecrease=min(TotalRevChange)
IncreaseDate=date[TotalRevChange.index(GIncrease)]
DecreaseDate=date[TotalRevChange.index(GDecrease)]
CountMonths=len(set(date))

with open ('Financial Report' '.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("------------------------\n")
    text.write("Total Months:" + str(CountMonths) + "\n")
    text.write("Total Revenue:" + "$" + str(TotalRev) + "\n")
    text.write("Average Revenue Change:" + "$" + str(int(AveRevChg)) + "\n")
    text.write("Greatest Increase in Revenue:" +str(IncreaseDate)+ "($" + str(GIncrease) + ")\n")
    text.write("Greatest Decrease in Revenue:" +str(DecreaseDate) + "($" + str(GDecrease) + ")\n\n")

