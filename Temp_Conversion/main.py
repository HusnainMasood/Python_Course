# =====================
# main.py: Converts degrees Fahrenheit into degrees Celsius
# By: Husnain Masood
# Modified: 2/18/2025
# =====================

# 1. Get temperature in degrees Fahrenheit 
degree_fahrenheit = float(input('Please enter a temperature in degrees Fahrenheit: '))
 
# 2. Calculate degress Celsius 
degree_celsius = (degree_fahrenheit - 32.0) * 5.0 / 9.0

# 3. Output the result and put a line space 
print('\nFor a Fahrenheit temperature of' , degree_fahrenheit, end='')
print(', the degrees Celsius is' , degree_celsius)
print('')   
