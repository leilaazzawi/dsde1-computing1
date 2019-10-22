print ('Please enter the length')
l = input()
if isinstance(l, str):
        print ('TypeError')
if input == 0:
        print ('ValueError')
print ('Please enter acceleration due to gravity')
g = input()
if isinstance(g, str):
        print ('TypeError')
if input == 0:
        print ('ValueError')
import math
T = math.pi*math.pow(l/g, 1/2)
print ('Time Period = ' + str(T))