"""
2. Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature.
The following formula is used for the conversion:
`C = (5 / 9) * (F - 32)`
"""

fahrenheit = float(input())
def temperature(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
    
print(temperature(fahrenheit))