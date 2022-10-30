Q = 1
def end():
    con = ()
    while con != 'Y' or con != 'N':
        print('Do you wish to continue with Code', Q, '? Y or N?')
        con = input()
        if con == 'Y':
            break
        else:
            exit()


print('Example 1: Write pseudo code that reads two numbers and multiplies them together and print out their product')
A = int(input('Number 1: '))
B = int(input('Number 2: '))
print('Total =', A * B)
Q = Q + 1
end()


print('Example 2: Write pseudo code that tells a user that the number they entered is not a 5 or a 6.')
C = int(input('Enter a Number: '))
if C != 5 and C != 6:
    print('The number is neither 5 or 6.')
else:
    if C == 5:
        print('Your number is 5.')
    if C == 6:
        print('Your number is 6')
Q = Q + 1
end()


print('Example 3: Write pseudo code that performs the following: Ask a user to enter a number. If the number is between 0')
print('and 10, write the word blue. If the number is between 10 and 20, write the word red. if the number is between')
print('20 and 30, write the word green. If it is any other number, write that it is not a correct color option.') 
D = int(input())
while D > 0:
    if D >= 0 and D < 10:
        print('Blue')
        break
    if D >= 10 and D < 20: 
        print('Red')
        break
    if D >= 20 and D < 30:
        print('Green')
        break
    if D >= 30:
        print('That is not a correct color option. Please add an input between 0 and 29')
        D = int(input())
Q = Q + 1
end()


print('Example 4: Write pseudo code to print all multiples of 5 between 1 and 100 (including both 1 and 100).')
E = 0
while E >= 0 and E <= 100:
    E = E + 1
    if E % 5 == 0:
        print(E)   
Q = Q + 1
end()


print('Example 5: Write pseudo code that will count all the even numbers up to a user defined stopping point.')
F = int(input())
G = 0
while G >= 0 and G <= F:
    G = G + 1
    if G % 2 == 0:
        print(G)
Q = Q + 1
end()


print('Example 6: Write pseudo code that will perform the following.') 
print('a) Read in 5 separate numbers.')
print('b) Calculate the average of the five numbers.')
print('c) Find the smallest (minimum) and largest (maximum) of the five entered numbers.')
print('d) Write out the results found from steps b and c with a message describing what they are')
H = ()
I = 0
listed = []
while I != 5:
    H = int(input())
    listed.append(H)
    I = I + 1
listed.sort()
listed.pop(1)
listed.pop(1)
listed.pop(1)
print('Average:', sum(listed) / 5)
print('[LOWEST #, HIGHEST #]')
print(listed)
Q = Q + 1
end()


print('Homework 1: Write pseudo code that reads in three numbers and writes them all in sorted order.')
J = ()
K = 0
listed = []
while K != 3:
    J = int(input())
    listed.append(J)
    K = K + 1
print(listed)
Q = Q + 1
end()


print('Homework 2: Write pseudo code that will calculate a running sum. A user will enter numbers that will be added to the') 
print('sum and when a negative number is encountered, stop adding numbers and write out the final result.')
L = int(input())
M = 0
while L >= 0:
    M = M + L
    L = int(input())
print('Total:', M)


print('Congrats! You went through all',Q,'codes I wrote in this one file.')
