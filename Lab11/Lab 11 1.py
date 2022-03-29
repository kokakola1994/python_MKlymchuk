A = [[1, 4], [-5, 8]]
print("A =", A)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))