import csv, tkinter as tk
import time

student_arr = []
binStudentArray = [] #bin heap of the student array

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
# s = [[str(e) for e in row] for row in student_arr]
# lens = [max(map(len, col)) for col in zip(*s)]
# fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
# table = [fmt.format(*row) for row in s]
# print('\n'.join(table))
#
# END Borrowed Code
#
select = 1


#
#
#Bin tree of the student array\ 0
#left = (i+1)*2-1|   1,3,7
#right = (i+1)*2|    2,6,14,30,62,126,254
#0
#1,2
#3,4,5,6
#7,8,9,10,11,12,13,14
#
numberOfStudents = len(student_arr)
null = ['0', '', '']
rootId = 0

def binArrayinsert(loc, arraySize, width, spot):
    #loc = spot in student_arr
    #spot = loc in binStudentArr
    # print(loc, spot)

    binStudentArray[spot] = student_arr[loc]
    if width == 1:
            return
    nextWidth = int(width/2)
    if (width % 2) != 0:
        if (nextWidth % 2) != 0:
            binArrayinsert(loc - int(nextWidth / 2) -1, arraySize, nextWidth, (spot + 1) * 2 - 1) # left
        else:
            binArrayinsert(loc - int(nextWidth / 2), arraySize, nextWidth, (spot + 1) * 2 - 1)  # left
        binArrayinsert(loc + int(nextWidth / 2) + 1, arraySize, nextWidth, (spot + 1) * 2)  # right
    else:
        if width == 2:
            binArrayinsert(loc + 1, arraySize, 1, (spot + 1) * 2)  # right
            return
        binArrayinsert(loc - int(nextWidth / 2), arraySize, nextWidth, (spot + 1) * 2 - 1)  # left
        binArrayinsert(loc + int(nextWidth / 2), arraySize, nextWidth-1, (spot + 1) * 2)  # right
    if width == 0:
        return
    return


if numberOfStudents > 0:
    treeSize = 1
    while treeSize < numberOfStudents:
        treeSize = treeSize*2 + 1
    for i in range(0, treeSize, 1):#fill arry with null values
        binStudentArray.append(null)
    print("bin Size:", len(binStudentArray))
    binArrayinsert(int(numberOfStudents / 2), numberOfStudents, numberOfStudents , 0)  # fill the array

# print("testing the bin tree")
# for i in range(0, len(binStudentArray), 1):
#     print(i, binStudentArray[i])

def binSearchMain(id, loc):
    if loc >= len(binStudentArray):
        return -1
    value = int(binStudentArray[loc][0])
    print(value, loc)
    if id == value: #if found done
        return binStudentArray[loc]
    else:
        if id < value:#if the id we are looking for is less than the value found
            return binSearchMain(id, (loc + 1) * 2 - 1)# left child of the current value (lesser value)
        else:
            return binSearchMain(id, (loc + 1) * 2)#right child of the current value (greater value)
    return -1

def binSearch(id):
    return binSearchMain(id, 0)


def sequential(term):
    return 0


def SearchWithBinary(term):
    id = -1
    try:
        id = int(term)
        return binSearch(id)
    except(ValueError):
        return sequential(term)
    return

start = time.time()
for i in range(0,100,1):
    print("Bin Search:",SearchWithBinary("21001"))
print("Bin Search 100 Times:", time.time()-start)


# exit(0)
#bin tree complete
#Bin Search 100 Times: 0.006976604461669922
#
#

#TODO: implement the search that uses bin heap
#TODO: make a function that can fill an array with some random numbers (for test searches)
#TODO: function that runs test searches and records the runtime or number of opperations
#TODO: Graph the data
#TODO: Show that the bin+sequential sort is faster


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
    start = time.time()
    for i in range(0, 100, 1):
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
    print("Sequential search time",time.time()-start)
    print("Sequential search ran through " + str(complexity) + " elements.")
    print("Efficiency is O(" + str(int(complexity/n)) + "N).\n\n")

    start = time.time()
    for i in range(0, 100, 1):
        print(":: 1st Closest: " + str(phpSearch(term, n)))
        print("\n\n")
    print("php search time", time.time() - start)

    try:
        select = int(input("Repeat? 0 for no: "))
    except(ValueError):
        select = 1

#123456
#Bin Search 100 Times: 0.00796365737915039
#Sequential search time 0.05586671829223633
#php search time 0.4642524719238281

#123456
#Bin Search 100 Times: 0.00797414779663086
#Sequential search time 0.05486893653869629
#php search time 0.30833911895751953

#21001
#Bin Search 100 Times: 0.0009810924530029297
#Sequential search time 0.05486941337585449
#php search time 0.3209042549133301

#21001 laptop
#Bin Search 100 Times: 0.004515647888183594
#Sequential search time 0.09026551246643066
#php search time 0.7609031200408936