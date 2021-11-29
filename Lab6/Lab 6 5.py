l = []
for i in range(0,31): l.append(3**i - 2**i)
l2 = []
for i in l: l2.append(i%19)
print("Input number from 0 to 18: ")
x = int(input())
if x > 18:
    print("Number > 18", end="\n")
elif x < 0:
    print("Number < 0", end="\n")
if x in l2:
    print("This number in list l2")
else:
    print("List l2 dont have this number")