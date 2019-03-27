#request user input
num = int(input('Please enter a number in range of 0...9999: '))

#attenuate numbers if neccessary
#Make sure number is not too small
if num < 0:
    num = 0

# make sure number is not too high
if num > 9999:
    num = 9999
    
#print the left brace
print(end = '[')

#extract and replace thousand-place digit
#determine thousand-place digit
digit = num//1000
#print thousand-place digit
print(digit, end = '')
#disccard thousand=place digit
num %= 1000

#extract and replace hundred-place digit
#determine hundred-place digit
digit = num//100
#print hundred-place digit
print(digit, end = '')
#disccard hundred=place digit
num %= 100

#extract and replace thousand-place digit
#determine ten-place digit
digit = num//10
#print ten-place digit
print(digit, end = '')
#disccard ten=place digit
num %= 10

#remainder is the one-place digit
#print the one-place digit
print(num, end = '')

#print right brace
print(end = ']')

