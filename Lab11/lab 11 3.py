from pprint import pprint
from random import randint

def losowa(a, b, n):
    gen_value = lambda decimals: randint(0,10)
    return [[gen_value(n) for _ in range(a)] for _ in range(b)]

def dodaj(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        res.append(row)
    return res


pprint(losowa(5, 5, 10))
print(end='\n')
A = losowa(5,5,10)
B = losowa(5,5,10)
print('A = ', end='\n')
pprint(A)
print('B = ', end='\n')
pprint(B)
print('Sum A+B = ', end='\n')
pprint(dodaj(A,B))