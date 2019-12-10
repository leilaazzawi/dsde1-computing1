
import math
def period(l, g):
        # print(type(l))
        if isinstance(l,str) or isinstance(g, str):
                raise TypeError ('please enter two numbers')
        if l == 0 or g == 0:
                raise ValueError ('please enter non-zero numbers')
        T = 2*math.pi*math.pow(l/g, 1/2)
        print ('Time Period = ' + str(T))
        return T

# time_period(123, 'abc')

