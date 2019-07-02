while True:
    txt = input("enter a your name: ")
    print(len(txt))
    if len(txt)<8:
        print("again?")
    else:
        print("t.y")
        break