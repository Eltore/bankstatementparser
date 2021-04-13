import csv
import sys

import names


def read_csv(file_name, folder_path):
    date_row = 1    # Change these three variables according to your csv file
    amount_row = 2  # If these aren't in the same order in your csv, change
    payee_row = 4   # the order in name_cleaner(), too.
    recipient_row = 5
    path = folder_path + file_name + '.csv'

    try:
        with open(path) as csvFile:
            csv_reader = csv.reader(csvFile, delimiter=';')
            modified_csv = []
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are \t{row[date_row]} | {row[amount_row]} | {row[recipient_row]}')
                    lines_to_add = [row[date_row], row[amount_row], row[recipient_row]]
                    line_count += 1

                    modified_csv.append(lines_to_add)
                else:
                    print(f'\t{row[date_row]} | {row[amount_row]} | {row[recipient_row]}.')
                    line_count += 1

                    if row[amount_row][0] == "-":
                        lines_to_add = [row[date_row], row[amount_row], row[recipient_row]]
                    elif row[amount_row][0] == "+":
                        lines_to_add = [row[date_row], row[amount_row], row[payee_row]]

                    modified_csv.append(lines_to_add)
        write_csv(clean_data(modified_csv), file_name, folder_path)
        print(f'Processed {line_count} lines.')
    except FileNotFoundError:
        print(f'{path} was not found by CSVCleaner.py.')
        sys.exit()


def write_csv(data, file_name, path):
    path = f'{path}/output{file_name}.csv'

    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerows([line])


def clean_data(data):
    cleaned_data = []

    for line in data:
        cleaned_data.append(name_cleaner(line))

    return cleaned_data


def name_cleaner(line):
    for name in names.list_of_names:
        title_case_line = line[2].title()

        if name in title_case_line:
            return [line[0], line[1], name]

    for k, v in names.special_cases.items():
        title_case_line = line[2].title()

        if k in title_case_line:
            return [line[0], line[1], v]

    return line


def main(file_name, path):
    read_csv(file_name, path)


if __name__ == '__main__':
    main('change_me.csv', 'change/me/')  # For manual operation without ProcessCSV.py
