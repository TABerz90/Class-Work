import random
x = int(input('How many random numbers do you want to generate: '))
y = int(input('From how many random numbers do you want to generate: '))
a = []
b = 0
print('Starting random number generation...')
while len(a) <= x:
    b = random.randint(0, y)
    if b in a:
        continue
    else:
        a.append(b)
print('Random Numbers Generated:')
print(a)
