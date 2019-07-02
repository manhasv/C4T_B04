while True:
    txt = input("enter a your name: ")
    print(txt)
    if txt.isalpha():
        print("t.y")
        break
    else:
        print("again?")
