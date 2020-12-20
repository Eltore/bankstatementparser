import csv


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
    with open('.data/analyzerOutput.csv', "a", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerows([line])


def analyze(data):
    totalspent = 0
    totalincome = 0

    for row in data:
        print(f'\t{row[0]} | {row[1]} | {row[2]}.')

        if row[1][0] == "-":
            numberline = row[1][1:].replace(',', '.')
            totalspent += float(numberline)
        elif row[1][0] == "+":
            numberline = row[1][1:].replace(',', '.')
            totalincome += float(numberline)
    monthsummary = [(f'{data[0][0][3:5]}/{data[0][0][6:]}', f'{totalincome}', f'{totalspent}')]
    return monthsummary


csvdata = readcsv()
monthdata = analyze(csvdata)
writecsv(monthdata)