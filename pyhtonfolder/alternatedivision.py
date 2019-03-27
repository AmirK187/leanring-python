# get two integers from user
dividend = int(input('Please enter number to divide: '))
divisor = int(input('Please enter second number to divide: '))
#if possible, divide them and report result
if divisor != 0:
    qoutient = dividend/divisor
    print(dividend, '/', divisor, '=', qoutient)
    print('Program finished')
