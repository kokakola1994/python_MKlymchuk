import random

def sotruj(lista):
    lenght = len(lista)
    for i in range(lenght): 
        for j in range(0, lenght-i-1):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
                
lista = []
listaslow = ['ala', 'ma', 'kota']

for i in range(0,10):
    n = random.randint(1,100)
    lista.append(n)

print("List lista with 10 random elements before buble sort:\n ", lista)
sotruj(lista)
print("List lista after using sort function :\n ", lista)
print("List listaslow before buble sort:\n ", listaslow)
sotruj(listaslow)
print("List listaslow after using sort function :\n ", listaslow)