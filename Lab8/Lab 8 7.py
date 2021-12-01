fo = open("p.txt", "r")
fo2 = open("p2.txt", "w")
for line in fo:
    lines = line.replace('z', 'Z')
    fo2.write(lines)
fo.close()
fo2.close()