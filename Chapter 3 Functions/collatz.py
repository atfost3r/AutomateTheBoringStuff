#This is to define the 

def collatz(number):
    numCheck = number % 2 
    if numCheck == 1:
        number = (3 * number) + 1
        return int(number)
    else:
        number = (number // 2)
        return int(number)




#This is the user input section and loop until we get our answer

print('Time to kick off the Collatz problem!')
print('Please enter a number:')
number = int(input())

collatz(number)

while number != 1:
    collatz(number)

