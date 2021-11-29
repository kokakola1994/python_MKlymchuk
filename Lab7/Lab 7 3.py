def zmien(a,b):
    c = a
    a = b
    b = c
    return a,b

listab = [7,2]
print("List listab before function zmien(): ", listab)
print("List listab when function zmien() used: ", zmien(*listab))
print("List listab after function zmien(): ", listab)