user_input = input('Type a number that is divisable by 3 or 5: ')
number = int(user_input)

if((number % 3 == 0) and (number % 5 == 0)):
    print('Fizz Buzz')
elif(number % 3 == 0):
    print('Fizz')
elif(number % 5 == 0):
    print('Buzz')
else:
    print('Not in the 3 or 5 times tables')
    
