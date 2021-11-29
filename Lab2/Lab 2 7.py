n=int(input())
k = int(n ** 0.5) + 2
prime = [True] * k
prime[0] = prime[1] = False
i = 1
while i*i < n + 1 :
    i += 1
    if not prime[i]:
        continue
    for j in range(i * i, k, i):
        prime[j] = False 
quat = [i*i for i in range(k) if prime[i]]
if n in quat :
    print('Yes')
else :
    print('No')