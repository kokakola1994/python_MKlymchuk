def zmien(a,b):
    c = a
    a = b
    b = c
    return a,b

print("Input variables x and y")
x = int(input())
y = int(input())
print("Vriable x:", x," y: ", y)
print("Variable in function zmien(): ",zmien(x,y))
print("Vriable x:", x," y: ", y," outside function")