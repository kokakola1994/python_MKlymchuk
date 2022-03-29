file = open('liczby.txt','r')
l = []
s = list(file.readlines())
i = 0
while i < len(s):
    l.append(s[i])
    i += 1
print(l)