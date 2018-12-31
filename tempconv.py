#this is a temperature conversion code from a python book
#Converts degrees Fahrenheit to degrees Celsius
#file is tempconv.py
#author: Rick Halterman
#formula found on
#http://en.wikipedia.org/Conversion_of_units_of_temperature

#Prompt user for temperature to convert and read the supplied value
degreesF = float(input('Enter the temperature in degrees F: '))
#perform the conversion
degreesC =5/9*(degreesF-32)
#Report result
print(degreesF,'degrees F=',degreesC,'degrees C')