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
i = input('Podaj i: ')
j = input('Podaj j: ')
print(i,j,i+j)

#(4)
i = int(input('Podaj i: '))
j = int(input('Podaj j: '))
print(i,j,i+j)

#(5)
i = int(input('Podaj i: '))
j = int(input('Podaj j: '))
print(i%j)
print(i//j)

#(6)
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))
if a > 10:
    print(a)
if b > 10:
    print(b)
if c > 10:
    print(c)

#(7)
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

def parzystanieparzysta(x):
    if x%2==0:
        print(" Liczba parzysta ")
    else:
        print(" Liczba nieparzysta ")

parzystanieparzysta(a)
parzystanieparzysta(b)

#(8)
r = int(input("Podaj rok: "))
if r % 4==0 and r % 100 != 0:
    print("rok jest przestepny")
elif r%400==0:
    print("rok jest przestepny")
else:
    print("rok nie jest przestepny")

#(9)
a = float(input("Podaj liczbe: "))
print(int(a) , a%1)

#(10)
f = float(input("Podaj liczbe f: "))
g = float(input("Podaj liczbe g: "))
print(int(f) + g%1)
print(int(g) + f%1)

#(11)
i = int(input('Podaj i: '))
j = int(input('Podaj j: '))
if i**j > j**i:
    print(i," do ", j ,"równe ",i**j, " jest wienksze od ", j, " do ", i, " równe ", j**i)
else:
    print(j," do ", i ,"równe ",j**i, " jest wienksze od ", i, " do ", j, " równe ", i**j)

#(12)
def perwiastkikwadratowe(x,y):
    y = 1/y
    result = x ** y
    print(result)
    return result

def najwienkszaliczba(x,y,z):
    if x > y and x > z:
        print( "największa liczba jest", x)
    elif y >x and y > z:
        print( "największa liczba jest", y)
    else:
        print( "największa liczba jest", z)

najwienkszaliczba(perwiastkikwadratowe(2,2),perwiastkikwadratowe(3,3),perwiastkikwadratowe(5,5))




