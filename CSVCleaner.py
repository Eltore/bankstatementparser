import csv
import names


def readcsv():
    daterow = 1  # Change these three variables according to your csv file
    amountrow = 2  # If these aren't in the same order in your csv, change
    payeerow = 4  # the order in namecleaner(), too.
    recipientrow = 5

    with open('.data/export.csv') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=';')
        modifiedcsv = []
        linecount = 0

        for row in csvreader:
            if linecount == 0:
                print(f'Column names are \t{row[daterow]} | {row[amountrow]} | {row[recipientrow]}')
                linestoadd = [row[daterow], row[amountrow], row[recipientrow]]
                linecount += 1

                modifiedcsv.append(linestoadd)
            else:
                print(f'\t{row[daterow]} | {row[amountrow]} | {row[recipientrow]}.')
                linecount += 1

                if row[amountrow][0] == "-":
                    linestoadd = [row[daterow], row[amountrow], row[recipientrow]]
                elif row[amountrow][0] == "+":
                    linestoadd = [row[daterow], row[amountrow], row[payeerow]]

                modifiedcsv.append(linestoadd)
    writecsv(cleandata(modifiedcsv))
    print(f'Processed {linecount} lines.')  # For debugging purposes


def writecsv(data):
    with open('.data/output.csv', "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerows([line])


def cleandata(data):
    cleaneddata = []

    for line in data:
        cleaneddata.append(namecleaner(line))

    return cleaneddata


def namecleaner(line):
    for name in names.listofnames:
        titlecaseline = line[2].title()

        if name in titlecaseline:
            return [line[0], line[1], name]

    for k, v in names.specialcases.items():
        titlecaseline = line[2].title()

        if k in titlecaseline:
            return [line[0], line[1], v]

    return line


readcsv()
