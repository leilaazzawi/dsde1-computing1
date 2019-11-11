print ('Please enter the length')
l = input()
print ('Please enter acceleration due to gravity')
g = input()

import math
def time_period(l, g):
        if type(l) != float or type(g) != float:
                raise TypeError
                print('please enter two numbers')
        if l == 0 or g == 0:
                raise ValueError
                print('please enter non-zero numbers')
        T = math.pi*math.pow(l/g, 1/2)
        print ('Time Period = ' + str(T))
        return T

time_period(l, g)

