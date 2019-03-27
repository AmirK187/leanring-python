#file bestterdivision.py
#get two integers from user
print('Please enter two numbers to divide.')
dividend = int(input('Please enter the first number to divide: '))
divisor = int(input('Please enter second number to be to divide: '))
# if possible, divide them and report result
if divisor != 0:
    print(dividend, '/', divisor, '=', dividend/divisor)
    