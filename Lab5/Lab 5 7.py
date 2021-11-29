from math import pi
text = "%.49f" % pi
digits = [int(s) for s in text if s != "."]
print('List of 50 digits pi number: ', digits)