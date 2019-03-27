#file timeconvcond2.py

#useful conversion factors
seconds_per_minute = 60
seconds_per_hour = 60 * seconds_per_minute #3600

#get user input in seconds
seconds = int(input("Please enter the number of seconds: "))

#1st, compute thenumber of hours in given number of seconds
hours = seconds // seconds_per_hour #3600 seconds = 1 hour

#compute the remaining seconds after the hours are accounted for
seconds = seconds % seconds_per_hour

#compute number of minutes in remaining seconds
minutes = seconds // seconds_per_minute #60 seconds = 1 minute

#compute remaining seconds after minutes are accounted for
seconds = seconds % seconds_per_minute

#report results
if hours > 0:
    print(hours, end = '')

#deciding between singular and plural
    if hours == 1:
        print(" hour ", end = '')
    else:
        print(" hours ", end = '')
    
if minutes > 0:
    print(minutes, end = '')

#deciding between singular and plural
    if minutes == 1:
        print(" minute ", end = '')
    else:
        print(" minutes ", end = '')

if seconds > 0 or (hours == 0 and minutes == 0 and seconds == 0):    
    print(seconds, end = '')

#deciding between singular and plural

    if seconds == 1:
        print(" second ", end = '')
    else:
        print(" seconds ", end = '')
print()