def zera(a,b):
    A=[[0 for i in range(a)] for j in range(b)]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))

zera(4,4)
print(end='\n')