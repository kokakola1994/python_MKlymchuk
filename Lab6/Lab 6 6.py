from math import factorial
l = []
for i in range (1,101): l.append(1/i)
print("Sum for all list l elements: ", sum(l))
print("The minimum element for list l: ", min(l))
print("The maximum element for list l: ", max(l))
n = 1000
factn = factorial(n)
s = str(factn)
lz = list(map(int,s))
print("Sum for all list lz elements 1000!: ", sum(lz))
