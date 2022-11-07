# s <--- 'Computer Science'
s = 'Computer Science'

# LEFT('Computer Science', 8)
p = s[0:8]
print(p)

# RIGHT('Comouter Science', 7)
z = s[-1:-8]
print(z)

# MID('Computer Science', 13, 5)
# ERROR in this situation
# Else
d = s[5:8]
print(d)

# LENGTH('Computer Science') + 1
x = len(s) + 1
print(x)

# TO_UPPER('Computer Science')
w = s.upper()
print(w)

# TO_LOWER('COMPUTER SCIENCE')
r = s.lower()
print(r)
