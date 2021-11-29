r=10
for x in range(-r, r + 1):
    for y in range(-r, r + 1):
        d = (x**2 + y**2)**0.5
        print(" " if d >= r else "*", sep='', end='' if y < r else '\n')
        
print('')

def prime(number):
    n = number
    counter = 0
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            d=(i**2 + j**2)**0,5
            print(" " if d >= r else "*", sep='', end='' if j < r else '\n')

prime(10)