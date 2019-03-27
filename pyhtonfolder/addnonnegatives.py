# ALlow the user to enter a sequence of nonnegative
#integers. The user ends the list with a negative
#integer. At the end the sum of the nonnegative
#numbers entered is displayed. The program prints
#zero if the user provides no nonnegative numbers.

#ensure loop is entered 
entry = 0
#initialise sum 
sum = 0
#request input
print ("Enter numbers to sum, negative number ends list:")

while entry >= 0:         #negative number exits loop
    entry = int(input()) #get value
    if entry >= 0:        #is number nonnegative?
        sum += entry      #add only if nonnegative  
print ("Sum =", sum)     #display sum 