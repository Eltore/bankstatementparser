import csv
import os.path
from datetime import datetime

import names
import pandas as pd
import matplotlib.pyplot as plt


def readcsv():
    with open('.data/output.csv') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=';')
        modifiedcsv = []
        linecount = 0

        for row in csvreader:
            if linecount == 0:
                linecount += 1
            else:
                print(f'\t{row[0]} | {row[1]} | {row[2]}.')
                linecount += 1
                modifiedcsv.append([row[0], row[1], row[2]])

    print(f'Processed {linecount} lines.')  # For debugging purposes
    return modifiedcsv


def writecsv(data):
    outputpath = '.data/analyzerOutput.csv'

    if os.path.isfile(outputpath):
        print('\nOutput file found. Adding new data to it...')

        with open(outputpath, "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerows([line])
        print('Successfully added new data to the output file.')
    else:
        print("\nFile 'analyzerOutput.csv' could not be found. Creating a new one...")
        data.insert(0, (['Date', 'Total income', 'Total spent', 'Net income', 'Food', 'Medicine', 'Rent', 'Subsidies']))

        with open(outputpath, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerows([line])
        print('Successfully created the output file.')


def addData(data):
    totalspent = 0
    totalincome = 0
    categories = {'Food': 0, 'Medicine': 0, 'Rent': 0, 'Subsidies': 0}

    for row in data:
        monetaryvalue = 0

        if row[1][0] == "-":
            monetaryvalue = float(row[1][1:].replace(',', '.'))
            totalspent += monetaryvalue
        elif row[1][0] == "+":
            monetaryvalue = float(row[1][1:].replace(',', '.'))
            totalincome += monetaryvalue

        for name in names.namecategories:
            if row[2] == name:
                categories[names.namecategories[name]] += monetaryvalue

    # TODO: Loop the categories instead of hardcoding them
    netincome = totalincome - totalspent
    monthsummary = [(f'{data[0][0][3:5]}/{data[0][0][6:]}', f'{totalincome:.2f}', f'{totalspent:.2f}', f'{netincome:.2f}', f"{categories['Food']}",
                     f"{categories['Medicine']}", f"{categories['Rent']}", f"{categories['Subsidies']}")]

    return monthsummary


analyzeData = 0  # input('Read new data from CSV before analyzing monthly data?\n0 = No\n1 = Yes\n')
if analyzeData == 1:
    csvdata = readcsv()
    monthdata = addData(csvdata)
    writecsv(monthdata)


def analyze():
    df = pd.read_csv('.data/analyzerOutput.csv', ';', index_col=0, parse_dates=True)
    print(df)
    df.plot(y=['Total income', 'Total spent', 'Net income'])
    plt.show()


analyze()
