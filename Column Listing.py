import numpy as np
names = []
marks = []
inn = input('Student Name: ')
inm = int(input('Student Marks: '))
while inm < 101 and inm > -1:
    names.append(inn)
    marks.append(inm)
    inn = input('Student Name: ')
    inm = int(input('Student Marks: '))
    if inm == 123:
        print('============================')
        print('[Name','Marks]')
        print(np.column_stack([names,marks]))
        print('----------------------------')
        print('Average of all class:', round(sum(marks)/len(marks),0))
        print('============================')
        break
