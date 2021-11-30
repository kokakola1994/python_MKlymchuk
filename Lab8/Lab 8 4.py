fo = open("p.txt", "r")
data = fo.read()
litleacount = data.count('a')
print("This program count small 'a' letters in .txt file: ", litleacount)