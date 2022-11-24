word = input('Enter Word: ')
last = len(word) - 1
print(len(word))
char = ''
char2 = ''
psuedo = False
counter = 0
while counter < len(word) + 1:
    char = word[last]
    char2 = word[counter]
    print(char2, char)
    if char != char2:
        print(word, 'is not Palindrome')
        psuedo = False
        break
    else:
        print(word, 'is Palindrome so far') 
        psuedo = True
    if last == counter:
        break        
    last -= 1        
    counter += 1  
if psuedo is True:
    print(word, 'is Palindrome.')          
