def sotruj(lista):
    lenght = len(lista)
    for i in range(lenght): 
        for j in range(lenght - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def sotrujbylenght(lista):
    lenght = len(lista)
    for i in range(lenght): 
        for j in range(lenght - i - 1):
            if len(lista[j]) > len(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

s = str(input("Input sentence: "))
l = s.split()
l1 = l.copy()
sotruj(l)
sotrujbylenght(l1)
print("Sentense sorted by alphabet: ", l, end="\n")
print("Sentense sorted by word lenght: ", l1, end=" ")