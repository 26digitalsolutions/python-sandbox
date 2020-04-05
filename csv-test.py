import csv

with open('csvfile.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    line_count = 0
    for row in csv_reader:

        if line_count == 0:
            print(f'Column names are {", ".join(row)} \n')

        print(row)

        line_count += 1
