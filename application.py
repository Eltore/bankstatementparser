import csv
import locale

locale.setlocale(locale.LC_ALL, "fi_FI")

def readCSV():
    with open('exportTest.csv') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=';')
        modifiedcsv = []
        linecount = 0
        moneygone = 0
        moneyin = 0

        for row in csvreader:
            if linecount == 0:
                print(f'Column names are \t{row[0]} | {row[2]} | {row[5]}')
                linestoadd = []
                linestoadd.append(row[0])
                linestoadd.append(row[2])
                linestoadd.append(row[5])
                linecount += 1

                modifiedcsv.append(linestoadd)
            else:
                print(f'\t{row[0]} | {row[2]} | {row[5]}.')
                linestoadd = []
                linestoadd.append(row[0])
                linestoadd.append(row[2])
                linestoadd.append(row[5])
                linecount += 1

                if row[2][0] == "-":
                    numberline = row[2][1:].replace(',', '.')
                    moneygone += float(numberline)
                elif row[2][0] == "+":
                    numberline = row[2][1:].replace(',', '.')
                    moneyin += float(numberline)

                modifiedcsv.append(linestoadd)
    writeCSV(modifiedcsv)
    print(f'Processed {linecount} lines. Money gone: {moneygone}. Money in: {moneyin}.')

def writeCSV(data):
    with open('output.csv', "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerows([line])

readCSV()