l = [0,1,2,3,4,5,6,7,8,9]
print('List l1: ', l)
l2 = l.copy()
l2.insert(9,l2.pop(0))
print('List l2 in which the starting list item is moved to the end: ', l2)
l3 = l.copy()
l3.insert(0,l3.pop(9))
print('List l3 the ending element of the list is moved to the beginning: ', l3)
l4 = l.copy()
l4[::-1] = l4
print('Inverted list l4: ', l4)
l5 = l.copy()
l5 = [x for x in l5 if not x%2]
print('List l5 with only even elements: ', l5)
l6 = l.copy()
l6 = [x for x in l6 if not l6[0] == x%2]
print('List l6 of odd items with even indexes: ', l6)