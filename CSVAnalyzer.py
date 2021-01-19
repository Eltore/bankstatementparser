import csv
import os.path
import names
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def readcsv():
    with open('ExampleCleaned.csv') as csvFile:
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
    outputpath = '.data/analyzerOutput.csv'  # Change to a preferred location

    if os.path.isfile(outputpath):
        print('\nOutput file found. Adding new data to it...')

        with open(outputpath, "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerows([line])
        print('Successfully added new data to the output file.')
    else:
        print("\nFile 'analyzerOutput.csv' could not be found. Creating a new one...")
        data.insert(0, (['Date', 'Total income', 'Total spent', 'Net income', 'Personal', 'Subsidies', 'Other income',
                         'Food', 'Utilities', 'Rent', 'Medicine', 'Clothes', 'Pets', 'Fun', 'Other spending']))

        with open(outputpath, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerows([line])
        print('Successfully created the output file.')


def addData(data):
    totalspent = 0
    totalincome = 0
    categories = {'Personal': 0, 'Subsidies': 0, 'Other income': 0,
                  'Food': 0, 'Utilities': 0, 'Rent': 0, 'Medicine': 0, 'Clothes': 0, 'Pets': 0, 'Fun': 0,
                  'Other spending': 0}

    for row in data:
        monetary_value = 0
        is_income = False
        category_was_found = False

        if row[1][0] == "-":
            monetary_value = float(row[1][1:].replace(',', '.'))
            totalspent += monetary_value
        elif row[1][0] == "+":
            monetary_value = float(row[1][1:].replace(',', '.'))
            totalincome += monetary_value
            is_income = True

        for name in names.namecategories:
            if row[2] == name:
                categories[names.namecategories[name]] += monetary_value
                category_was_found = True
                break

        if not category_was_found:
            if is_income:  # TODO: A better way to solve unknown names
                categories['Other income'] += monetary_value  # Add positive amounts to other income
                print(f'{monetary_value} was added to other income.')
            else:
                categories['Other spending'] += monetary_value  # Add negative amounts to other spending
                print(f' {monetary_value} was added to other spending.')


# TODO: Loop the categories instead of hardcoding them
    netincome = totalincome - totalspent
    monthsummary = [(f'{data[0][0][3:5]}/{data[0][0][6:]}', f'{totalincome:.2f}', f'{totalspent:.2f}',
                     f'{netincome:.2f}', f"{categories['Personal']:.2f}", f"{categories['Subsidies']:.2f}",
                     f"{categories['Other']:.2f}", f"{categories['Food']:.2f}", f"{categories['Utilities']:.2f}",
                     f"{categories['Rent']:.2f}", f"{categories['Medicine']:.2f}", f"{categories['Clothes']:.2f}",
                     f"{categories['Pets']:.2f}", f"{categories['Fun']:.2f}", f"{categories['Other ']:.2f}")]

    return monthsummary


analyzeData = 1  # input('Read new data from CSV before analyzing monthly data?\n0 = No\n1 = Yes\n')
if analyzeData == 1:
    csvdata = readcsv()
    monthdata = addData(csvdata)
    writecsv(monthdata)


def analyze():
    df = pd.read_csv('.data/analyzerOutput.csv', ';', index_col=0, parse_dates=True)
    print(df)
    months = mdates.MonthLocator()  # every month
    days = mdates.DayLocator()  # every month
    dateFormat = mdates.DateFormatter('%m-%Y')

    # Net income graph
    df2 = df[['Total income', 'Total spent']]
    df3 = pd.DataFrame(df2.stack()).reset_index()
    df3.columns = ['Date', 'Type', 'Value']
    print(df3)

    g, ax = plt.subplots(figsize=(7, 5))

    # sns.lineplot(data=df3,
    #              x='Date', y='Value',
    #              hue='Type', ax=ax)

    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(dateFormat)
    ax.xaxis.set_minor_locator(days)

    g.autofmt_xdate()

    plt.show()


display_graphs = 0  # input('Create graphs based on data? \n0 = No\n1 = Yes\n')
if display_graphs == 1:
    analyze()
