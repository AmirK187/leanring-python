#learning python

#Some definitions
# operand = data to be manipulated or oprated on
# truncate = shorten or reduce



# The program calculates area of rectangle
l=8
b=5
a=l*b
print("Area of rectangle is",  a)
#press f5 to run/test.

#just prctice
message="Hello World!"
print(message)
print(10)
print('Hello World!\
It might rain today.\
Tommorow is sunday.')
print('''Hello World!
It might rain today.
Tomorrow is sunday.''')

#learning python aritnmetic(basics of math)

#division(//) usage of 2 forward /.
#random ex. basic
a=4
b=8
c=b//a
print("c is ",c)
#alittle bit harder. Single / allows for decimal places
d=3.0
e=7.0
f=e/d
print("f is %.2f" %f)#%.2f allows for 2 deccimal places, can add 6 after . allows for decimal place.

#exponentiation
#the use of double asterisks(**).
#example
# a**b == a to the power b.
a=4
b=2
a**b
print(a**b)
#alittle more harder
#using pi to calculate volume of a sphere
#example
from math import pi #value for pi is 3.1416 round to 4 decimal places.
r=3                 #r represents radius
v=4/3*pi*pow(r,3)  #pow() is same as r**3
print("Volume of sphere is %.2f" %v)

#data types
# data type is a function used to determine what type a object is.
#example
a=4
b=9.67
c=[a,b,c]
d=('mom','dad','son')
e="Good day"
f=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
