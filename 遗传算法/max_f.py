from math import *
import sys

num = 10000
X = [i + j / num for i in range(11) for j in range(num)]
max_value = -sys.maxsize
max_x = 0
for x in X:
    y = x + 2 * sin(2 * x) + 3 * sin(3 * x) + 4 * sin(4 * x)
    if max_value < y:
        max_value = y
        max_x = x
print('max{f(x)}=', max_value, ' x= ', max_x)

