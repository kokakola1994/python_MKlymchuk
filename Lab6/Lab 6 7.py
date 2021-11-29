from math import factorial
def find_pairs_of_numbers(num_list,n):
    count = 0
    for num1 in num_list:
        for num2 in num_list:
            if (num1 + num2) == n:                
                count = count + 1
    return int(count/2)

n = 1000
factn = factorial(n)
s = str(factn)
lz = list(map(int,s))
for i in range(1,100): print(i, "- wystempuje " ,find_pairs_of_numbers(lz,i), " razy")