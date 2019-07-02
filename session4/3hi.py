while True:
    txt = input("enter a number ")
    print(txt)
    if txt.isdigit():
        print("t.y")
        break
    else:
        print("again?")
print(2018 - int(txt))