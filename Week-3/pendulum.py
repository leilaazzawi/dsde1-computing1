print ('Please enter the length')
l = input()
if type(l) != int:
        print('TypeError')
if input == 0:
        print('ValueError')
print ('Please enter acceleration due to gravity')
g = input()
if type(g) != int:
        print('TypeError')
if input == 0:
        print('ValueError')
import math
T = math.pi*math.pow(l/g, 1/2)
print ('Time Period = ' + str(T))