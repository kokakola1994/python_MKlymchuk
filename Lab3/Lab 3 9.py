for i in range(1,11):
    for j in range(1,11):
        if i**j>j**i:
            print(f'{">":2}', end=" ")
        elif i**j==j**i:
            print(f'{"=":2}',end=" ")
        else:
            print(f'{"<":2}',end=" ")
    print()