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

print('Input number of elements in list, and then input this element: ')
n = int(input())
l = []
for i in range(0,n): 
    num = int(input())
    l.append(num)
print('List l elements:', l)

print('The largest element in list: ', max(l))
print('The smallest element in list: ', min(l))     