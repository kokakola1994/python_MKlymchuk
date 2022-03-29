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

def pomnoz(a,b):
    c = []
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)

    return c

pprint(losowa(5, 5, 10))
print(end='\n')
A = losowa(5,5,10)
B = losowa(5,5,10)
print('A = ', end='\n')
pprint(A)
print('B = ', end='\n')
pprint(B)
print('Multiply A+B = ', end='\n')
pprint(pomnoz(A,B))