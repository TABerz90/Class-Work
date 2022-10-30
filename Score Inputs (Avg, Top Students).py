mark = []
boola = []
boolb = []
inpa = ()
inpb = ()
while len(mark) != 7:
    inpb = input('Name: ')
    inpa = int(input('Marks: ')) 
    if inpa >= 80:
        boolb.append(inpb)
        boola.append(inpa)
    mark.append(inpa)
print('*************************')
print('AVERAGE OF ENTIRE CLASS')
print(sum(mark)//len(mark)) 
print('*************************')
print('STUDENTS WITH 80+ MARKS')
print(boolb)
print(boola)
print('*************************')
