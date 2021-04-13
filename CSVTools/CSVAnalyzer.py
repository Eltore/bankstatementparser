import csv
import os.path
import sys
import names


def read_csv(file_name, folder_path):
    path = folder_path + 'output' + file_name + '.csv'

    try:
        with open(path) as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=';')
            modified_csv = []
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    print(f'\t{row[0]} | {row[1]} | {row[2]}.')
                    line_count += 1
                    modified_csv.append([row[0], row[1], row[2]])

        print(f'Processed {line_count} lines.')
        return modified_csv
    except FileNotFoundError:
        print(f'{path} was not found by CSVAnalyzer.py.')
        sys.exit()


def write_csv(data, folder_path):
    output_path = folder_path + 'ExampleCleaned.csv'

    if os.path.isfile(output_path):
        print('\nOutput file found. Adding new data to it...')

        with open(output_path, "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerows([line])
        print('Successfully added new data to the output file.')
    else:
        print("\nFile 'ExampleCleaned.csv' could not be found. Creating a new one...")
        data.insert(0, (['Date', 'Total income', 'Total spent', 'Net income', 'Personal', 'Subsidies', 'Other income',
                         'Food', 'Utilities', 'Rent', 'Medicine', 'Clothes', 'Pets', 'Fun', 'Other spending']))

        with open(output_path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerows([line])
        print('Successfully created the output file.')


def add_data(data):
    total_spent = 0
    total_income = 0
    categories = {'Personal': 0, 'Subsidies': 0, 'Other income': 0,
                  'Food': 0, 'Utilities': 0, 'Rent': 0, 'Phones': 0, 'Medicine': 0, 'Clothes': 0, 'Pets': 0, 'Fun': 0,
                  'Other spending': 0}

    for row in data:
        monetary_value = 0
        is_income = False
        category_was_found = False

        if row[1][0] == "-":
            monetary_value = float(row[1][1:].replace(',', '.'))
            total_spent += monetary_value
        elif row[1][0] == "+":
            monetary_value = float(row[1][1:].replace(',', '.'))
            total_income += monetary_value
            is_income = True

        for name in names.name_categories:
            if row[2] == name:
                categories[names.name_categories[name]] += monetary_value
                category_was_found = True
                break

        if not category_was_found:
            if is_income:  # TODO: A better way to solve unknown names
                categories['Other income'] += monetary_value  # Add positive amounts to other income
                print(f'{monetary_value} ({row[2]}) was added to other income.')
            else:
                categories['Other spending'] += monetary_value  # Add negative amounts to other spending
                print(f'{monetary_value} ({row[2]}) was added to other spending.')

    # TODO: Loop the categories instead of hardcoding them
    net_income = total_income - total_spent
    month_summary = [(f'{data[0][0][3:5]}/{data[0][0][6:]}', f'{total_income:.2f}', f'{total_spent:.2f}',
                      f'{net_income:.2f}', f"{categories['Personal']:.2f}", f"{categories['Subsidies']:.2f}",
                      f"{categories['Other income']:.2f}", f"{categories['Food']:.2f}", f"{categories['Utilities']:.2f}",
                      f"{categories['Rent']:.2f}", f"{categories['Phones']:.2f}", f"{categories['Medicine']:.2f}",
                      f"{categories['Clothes']:.2f}", f"{categories['Pets']:.2f}", f"{categories['Fun']:.2f}",
                      f"{categories['Other spending']:.2f}")]

    return month_summary


def main(file_name, path):
    csv_data = read_csv(file_name, path)
    month_data = add_data(csv_data)
    write_csv(month_data, path)


if __name__ == '__main__':
    main('change_me.csv', 'change/me/')  # For manual operation without ProcessCSV.py
