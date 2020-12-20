import csv


# Names that will be simplified, e.g. K Citymarket Espoo Sello -> K Citymarket
listofnames = ['Alko', 'K Citymarket', 'Prisma', 'K Market', 'K Supermarket', 'Lidl', 'Burger King',
               'Alepa', 'Juho', 'Ella']

# Names that will be changed to better reflect what they are
specialcases = {'Sefay': 'Pizzeria Online', 'Ya': 'Apteekki', 'Aalto': 'AYY', 'Kansanel': 'Kela'}


def readcsv():
    with open('.data/export.csv') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=';')
        modifiedcsv = []
        linecount = 0

        for row in csvreader:
            if linecount == 0:
                print(f'Column names are \t{row[1]} | {row[2]} | {row[5]}')  # Change the row indexes to the preferred
                linestoadd = [row[1], row[2], row[5]]                        # ones both in here and at namecleaner()
                linecount += 1

                modifiedcsv.append(linestoadd)
            else:
                print(f'\t{row[1]} | {row[2]} | {row[5]}.')
                linecount += 1

                if row[2][0] == "-":
                    linestoadd = [row[1], row[2], row[5]]
                elif row[2][0] == "+":
                    linestoadd = [row[1], row[2], row[4]]

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
    for name in listofnames:
        titlecaseline = line[2].title()

        if name in titlecaseline:
            return [line[0], line[1], name]

    for k, v in specialcases.items():
        titlecaseline = line[2].title()

        if k in titlecaseline:
            return [line[0], line[1], v]

    return line


readcsv()
