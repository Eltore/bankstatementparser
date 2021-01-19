import csv
import names


def read_csv(file_to_read):
    date_row = 1  # Change these three variables according to your csv file
    amount_row = 2  # If these aren't in the same order in your csv, change
    payee_row = 4  # the order in name_cleaner(), too.
    recipient_row = 5
    path = '.data/CSVs/' + file_to_read + '.csv'

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
    write_csv(clean_data(modified_csv), file_to_read)
    print(f'Processed {line_count} lines.')  # For debugging purposes


def write_csv(data, file_to_read):
    path = f'.data/output{file_to_read}.csv'

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
    for name in names.listofnames:
        titlecase_line = line[2].title()

        if name in titlecase_line:
            return [line[0], line[1], name]

    for k, v in names.specialcases.items():
        titlecase_line = line[2].title()

        if k in titlecase_line:
            return [line[0], line[1], v]

    return line


filename = 'Not empty'
while filename != '':
    filename = input('Enter the name of the file to be cleaned (enter blank to quit):\n')
    if not filename == '':
        read_csv(filename)
