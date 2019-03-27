#converting and 10 base into a 2 base binary number using if statement
#get number from user
value = int(input('Please enter a integer value in the range of 0...1023: '))

#create an empty binary string to build on
binary_string = ''

#integer has to be less than 1024
if 0 <= value < 1024:
    binary_string += str(value//512)
    value %= 512
    binary_string += str(value//256)
    value %= 256
    binary_string += str(value//128)
    value %= 128
    binary_string += str(value//64)
    value %= 64
    binary_string += str(value//32)
    value %= 32
    binary_string += str(value//16)
    value %= 16
    binary_string += str(value//8)
    value %= 8
    binary_string += str(value//4)
    value %= 4
    binary_string += str(value//2)
    value %= 2
    
#display result
if binary_string != '':
    print(binary_string)
else:
    print('Cannot convert.')    