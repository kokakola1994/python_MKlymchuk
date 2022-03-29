import random

random_float_list = []
# Set a length of the list to 10
for i in range(0, 100):
    # any random float between 50.50 to 500.50
    # don't use round() if you need number as it is
    x = round(random.uniform(22, 26), 2)
    random_float_list.append(x)

print(random_float_list)
with open('a_file.txt', 'w') as f:
    for item in random_float_list:
        f.write("%s\n" % item)

# Output [98.01, 454.48, 117.69, 51.44, 415.01, 455.52, 65.39, 385.07, 112.38, 434.1]