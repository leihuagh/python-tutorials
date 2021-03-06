# This program uses the csv module to manipulate .csv files

import csv

# Reader Objects
exampleFile = open("example.csv")
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

print(exampleData[0][0])
print(exampleData[0][1])
print(exampleData[0][2])
print(exampleData[1][1])
print(exampleData[6][1])

# Reading Data from Reader Objects in a for Loop
exampleFile = open("example.csv")
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print("Row #" + str(exampleReader.line_num) + ' ' + str(row))
