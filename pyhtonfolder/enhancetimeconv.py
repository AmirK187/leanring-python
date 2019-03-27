#converting seconds to hours, minutes and seconds. Readable time.
#file enhancetimeconv.py

# The number of seconds 
seconds = int(input('Please enter the number of seconds: '))
#1st, convert the number of seconds to hours
#integer division with possible truncation
#3600 seconds = 1 hour
hours = seconds // 3600
#compute remainder seconds after hours are counted for
seconds = seconds % 3600
#60 seconds = 1 minute
#compute remainder seconds to minutes
minutes =  seconds // 60
#compute remainder seconds sfter minutes counted for
seconds = seconds % 60
#report results
print(hours, ':', sep = '', end = '')
#compute tens digit of minutes
tens = minutes // 10
#computes ones digits of minutes
ones = minutes % 10
print(tens, ones, ':', sep = '', end = '')
#compute tens digit of seconds
tens = seconds // 10
#computes ones digit of seconds
ones = seconds % 10
print(tens, ones, sep = '')