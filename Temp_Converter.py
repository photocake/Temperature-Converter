import os

print('This is a simple temperature converter, it can convert Celsius temperature into Fahrenheit temperature.')

c_temp = input('Please input Celsius temperature :')
c_temp = float(c_temp)
f_temp = c_temp * 9 / 5 + 32
print('Fahrenheit temperature is', f_temp, 'degress.')

os.system("pause")