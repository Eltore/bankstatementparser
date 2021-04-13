from CSVTools import CSVCleaner
from CSVTools import CSVAnalyzer


def main():
    filename = 'Not empty'
    path = input("Set path to the folder where the CSVs are located with the last '/' included:\n")
    while filename != '':
        filename = input('Enter the name of the file to be cleaned (enter blank to quit):\n')
        if not filename == '':
            CSVCleaner.main(filename, path)
            CSVAnalyzer.main(filename, path)


if __name__ == '__main__':
    main()
