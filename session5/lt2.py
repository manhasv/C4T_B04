month = int(input("ur month (num) : "))
if month == 2 :
    print(28)
elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print(31)
else:
    print(30)