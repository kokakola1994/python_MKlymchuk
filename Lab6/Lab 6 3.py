from math import factorial
n = 1000
print("Factorial list ls for 1000!: ", end="\n")
factn = factorial(n)
s = str(factn)
ls = list(s)
for i in range(1,10): print("Number of digits ", i , ':', ls.count(str(i)))
print("Factorial list ls for 2000!: ", end="\n")
n2 = 2000
factn = factorial(n2)
s2 = str(factn)
ls2 = list(s2)
for i in range(1,10): print("Number of digits ", i , ':', ls2.count(str(i)))