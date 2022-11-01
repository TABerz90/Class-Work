import random as rand
a = []
b = 0
while len(a) <= 10:
    b = rand.randint(0,100)
    if b in a:
        print(b, 'is already in array.')
    else:
        a.append(b)   
        print(b, 'is added to array')       
print(a)
print('SORTING')
e = 0
f = 0
while e != 11:
    c = 0
    d = 1
    while d <= 10:
        g = a[c]
        h = a[d]
        if g > h:
            f = g
            a.pop(c)
            a.insert(d, f)
        d = d + 1
        c = c + 1
        if d > 11:
            break
    e = e + 1
    print(a)
print('FINAL SORTED')
print(a)
