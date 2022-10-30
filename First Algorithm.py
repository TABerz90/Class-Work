low = 0
total = int(input("What is the highest number you want? "))
high = total #high will constantly be updated in the while loop so we need another fixed variable
item = int(input('What is to be guessed? '))
guess = 0
while high >= low:
    mid = (low + high) // 2
    position = mid + 1
    guess = guess + 1    #The total number of guesses it took to find the input value
    if mid == item:     #If the guess is correct
        print('*********************************************************')
        print('Number that was to be guessed: ', item, '/', total)
        print('Position in List:', position)
        print('Number of Guesses taken:', guess)
        print('*********************************************************')
        break
    elif mid > item:    #If the guess is higher
        high = mid - 1
        print('High! New Guess:', mid)
    elif mid < item:    #If the guess is lower
        low = mid + 1
        print('Low! New Guess:', mid)
