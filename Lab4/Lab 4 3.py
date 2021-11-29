print('Write a sentence')
str = input()
for i in str :
    if i == ' ' :
        print('\n')
    else :
        print(i,end='')
print('\n','Sentens lenght: ', len(str))