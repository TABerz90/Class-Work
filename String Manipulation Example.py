s = 'Computer Science'

e = 0

d = 0

x = 0

while e != len(s):

    if 'A' == s[x] or 'a' == s[x]:

        print(s[x])

        d = d + 1

    if 'E' == s[x] or 'e' == s[x]:

        print(s[x]) 

        d = d + 1  

    if 'I' == s[x] or 'i' == s[x]:

        print(s[x])  

        d = d + 1

    if 'O' == s[x] or 'o' == s[x]:

        print(s[x])

        d = d + 1

    if 'U' == s[x] or 'u' == s[x]:

        print(s[x])  

        d = d + 1

    x = x + 1

    e = e + 1

print(d)
