fo = open("p.txt", "a")
fo.write('\n' + input("Write new line to .txt file: "))
fo.write('\n' + input("Write second new line to .txt file: "))
fo.close()