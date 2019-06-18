#Bank Python Code
#import os and CSV
import os, os.path
import csv

#fn = pathlib.Path(__file__).parent / 'budget_data.csv'
#budget=os.join(cwd, "budget_data.csv")
#budget_length=len(budget)

  #Set empty list variables
    date = []
    revenue =[]
    month = []
    year =[]
    revenueChange =[]
    TotalRev =0
    TotalRevChange = 0
    RevBeg=0
    itemCount = 0
    
with open(budget,'r') as csvFile:
    csvReader=csv.reader(csvFile, delimiter=',')

#for numbers 