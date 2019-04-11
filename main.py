import csv, tkinter as tk

student_arr = []

with open('Students.csv', mode='r') as students:
    r = csv.DictReader(students)
    n = 0
    for row in r:
        curr_array = []
        #print(f'{row["first"]}\t\t{row["last"]}\t\t{row["email"]}')
        curr_array.append(row["email"])
        curr_array.append(row["id"])
        curr_array.append(row["last"])
        curr_array.append(row["first"])
        curr_array.append(row["grade"])
        n += 1
        student_arr.append(curr_array)
    print(f'Processed {n} lines.')


#
# Pretty Print Code:
#      Source: https://stackoverflow.com/questions/13214809/pretty-print-2d-python-list
#      Using temporatily for debugging
#
s = [[str(e) for e in row] for row in student_arr]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
#
# END Borrowed Code
#

select = 1

while(select):
    complexity = 0
    print("\n\n\n__________________________________________")
    term = str(input("Search term: "))
    found = False
    for i in range(n):
        for j in range(5):
            complexity += 1
            if(student_arr[i][j].lower() == term.lower()):
                print(student_arr[i])
                found = True
    if(found == 0):
        print("Could not find value.")

    print("Search ran through " + str(complexity) + " elements.\n\n")
    try:
        select = int(input("Repeat? 0 for no: "))
    except(ValueError):
        select = 1


