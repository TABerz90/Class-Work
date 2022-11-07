password = input('Insert Password: ')
char = ''
iteration = 0
tick_checks = 0
numbers = ['0','1','2','3','4','5','6','7','8','9']
a = [0, 0, 0] # I am using a second array to confirm that all conditions have been met. 
while iteration < len(password) + 1:
    char = password[iteration]
    if (char.isupper()) == True and a[0] != 1: # {a[0] != 1} basically means that if the condition has not already been fulfilled in this case.
        tick_checks += 1
        a.pop(0)
        a.insert(0, 1)
    elif (char.islower()) == True and a[1] != 2:
        tick_checks += 1
        a.pop(1)
        a.insert(1, 2)
    elif char in numbers and a[2] != 3:
        tick_checks += 1
        a.pop(2)
        a.insert(2, 3)
    iteration += 1
    if a == [1, 2, 3]: # If all conditions are met.
        print('Welcome!')
        break
    elif a != [1, 2, 3] and iteration == len(password):
        password = input('Invalid Password. Please Try again: ')
        iteration = 0 # Reset Iterations for another go.
