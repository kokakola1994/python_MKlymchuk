def max(l):
    max = l[0]
    for x in l:
        if x > max :
            max = x
    return max

def min(l):
    min = l[0]
    for x in l:
        if x < min :
            min = x
    return min

from math import sin
print('Input number of elements in list, and then input this element: ')
n = int(input())
l = []
for i in range(0,n): 
    num = int(input())
    l.append(sin(num))
print('List sin(l) elements: ', l)

print('The largest sin() element in list: ', max(l))
print('The smallest sin() element in list: ', min(l))     