def power(n, m):
    while m == 0:
        return 1
    else:
        return n * power(n, m - 1)
 
print(power(float(input()), int(input())))