#!/usr/bin/env python
import csv

inputFile = raw_input("Enter input file : ")
outputFile = raw_input("Enter output file : ")

setInitial = []
dictInitial = {}

with open(inputFile, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    noam = tuple(spamreader)
    for row in noam:
        if row[0] in setInitial:
            dictInitial[row[0]] += 1
        else:
            setInitial.append(row[0])
            dictInitial[row[0]] = 1

# print dictInitial

# for item in dictInitial:
#     print item + ' -- ' + str(dictInitial[item])

with open(outputFile, 'wb') as f:  # Just use 'w' mode in 3.x
    spamwriter = csv.writer(f, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in dictInitial:
        test = item + ';' + str(dictInitial[item])
        spamwriter.writerow([test])
