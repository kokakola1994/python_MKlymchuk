r = int(input("Podaj rok: "))
if r % 4==0 and r % 100 != 0:
    print("rok jest przestepny")
elif r%400==0:
    print("rok jest przestepny")
else:
    print("rok nie jest przestepny")