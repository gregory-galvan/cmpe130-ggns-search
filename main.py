import csv, tkinter as tk

student_arr = []

with open('Students.csv', mode='r') as students:
    r = csv.DictReader(students)
    n = 0
    for row in r:
        curr_array = []
        #print(f'{row["first"]}\t\t{row["last"]}\t\t{row["email"]}')
        curr_array.append(row["id"])
        curr_array.append(row["last"])
        curr_array.append(row["first"])
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

def phpSearch(term, n):
    cs = 0
    cs2 = 0
    cs3 = 0
    closest = 0
    c2 = 0
    c3 = 0
    iterations = 0
    for i in range(n):
        for j in range(3):
            term = term.lower()
            ct = student_arr[i][j].lower() #current value
            sl = len(ct)                   #length of current
            st = len(term)                 #term length
            score = 0
            don = 0
            rep = 0
            tmt = term[don]
            for k in range(sl):
                for m in range(st):
                    iterations += 1
                    if(ct[k] == tmt):
                        score += 1
                        if(rep != 0):
                            score = score + (rep * 2)
                        don += 1
                        rep += 1
                        if(don < st):
                            tmt = term[don]
                        break
                    else:
                        rep = 0
                        break
                    print("Done:    " + str(don))
                    print("Current: " + str(tmt))
            if(score > cs3):
                c3 = i
                cs3 = score
                if(cs3 > cs2):
                    cst = cs2
                    cs2 = cs3
                    cs3 = cst
                    ctt = c3
                    c3 = c2
                    c2 = ctt
                    if(cs2 > cs):
                        cst = cs2
                        cs2 = cs
                        cs = cst
                        ctt = closest
                        closest = c2
                        c2 = ctt
    print("Php search ran through " + str(iterations) + " elements.")
    print("Efficiency is O(" + str(int(iterations/n)) + "N).")
    print("3rd Closest: " + str(student_arr[c3]))
    print("2nd Closest: " + str(student_arr[c2]))
    return(student_arr[closest])
                    

while(select):
    complexity = 0
    print("\n\n\n__________________________________________")
    term = str(input("Search term: "))
    found = False
    nf = 0
    for i in range(n):
        for j in range(3):
            complexity += 1
            if(student_arr[i][j].lower() == term.lower()):
                nf += 1
                print(student_arr[i])
                found = True
    if(found == 0):
        print("\n!!! Could not find value with sequential.")
    print("--> Sequential search found " + str(nf) + " elements.")
    print("Sequential search ran through " + str(complexity) + " elements.")
    print("Efficiency is O(" + str(int(complexity/n)) + "N).\n\n")
    print(":: 1st Closest: " + str(phpSearch(term, n)))
    print("\n\n")
    try:
        select = int(input("Repeat? 0 for no: "))
    except(ValueError):
        select = 1

