fo = open("p.txt", "r")
s = str(input("Input word to search in .txt file: "))
for line in fo:
    if s in line:
        print("This word in this statment: ", line)
        break
else: print("This word not in .txt file(")
fo.close()