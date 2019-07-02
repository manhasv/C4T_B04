from random import randint
while True:
    z=randint(-1,1)
    x = randint(0,100)
    y = randint(0,100)
    c=x+y
    d = x+y+z
    print(x,"+",y,"=",d)
    inpu = input(" your answer(d/s): ")
    if d == c:
        if inpu == "d":
            print("Correct")
        else:
            print("Incorrect")
            break
    else:
        if inpu == "d":
            print("Incorrect")
            break
        else:
            print("Correct")
        