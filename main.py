import csv

with open('Students.csv', mode='r') as students:
    r = csv.DictReader(students)
    n = 0
    for row in r:
        if n == 0:
            print(f'Column names are {", ".join(row)}')
            n += 1
        print(f'{row["first"]}\t\t{row["last"]}\t\t{row["email"]}')
        n += 1
    print(f'Processed {n} lines.')
