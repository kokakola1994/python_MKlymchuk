#Python (1) -Zmienne, typy, print, input, if

#(1)
a=2
b=5
c=5.0
d=4.2
print(a,b,c,d)
print(a+b,a+c,a+d,a*b,a*c,a*d)

#(2)
s='kot'
t=" i pies"
print(s,t)
print(s+t,t+s+t,2*s)

#(3)
i = input('Podaj i')
j = input('Podaj j')
print(i,j,i+j)

#(4)
i = int(input('Podaj i'))
j = int(input('Podaj j'))
print(i,j,i+j)

#(5)
i = int(input('Podaj i'))
j = int(input('Podaj j'))
print(i%j)
print(i//j)

#(6)
a = int(input('Podaj a'))
b = int(input('Podaj b'))
c = int(input('Podaj c'))
if a > 10:
    print(a)
if b > 10:
    print(b)
if c > 10:
    print(c)

#(7)
a = int(input('Podaj a'))
b = int(input('Podaj b'))

def parzystanieparzysta(x):
    if x%2==0:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")

parzystanieparzysta(a)
parzystanieparzysta(b)

#(7)

