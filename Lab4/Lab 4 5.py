sum = 0
result = 0
print('Enter the number of digits for the average: ')
n = int(input())
print('Enter numbers: ')
for i in range(n) : x = int(input()); sum += x
result = sum/n
print('Average: ', result)