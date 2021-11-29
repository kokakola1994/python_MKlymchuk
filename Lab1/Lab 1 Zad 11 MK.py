i = int(input('Podaj i: '))
j = int(input('Podaj j: '))
if i**j > j**i:
    print(i," do ", j ,"równe ",i**j, " jest wienksze od ", j, " do ", i, " równe ", j**i)
else:
    print(j," do ", i ,"równe ",j**i, " jest wienksze od ", i, " do ", j, " równe ", i**j)