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