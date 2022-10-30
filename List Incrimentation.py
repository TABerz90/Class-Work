listed = [0]
g = 1
n = 1
s = int(input('What is the highest number that you would like? '))
while len(listed) <= s:
    n = n + 1
    g = g + 1
    listed.insert(g, n)
print(listed)
