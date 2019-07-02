name = input("ur name : ")
uname = input("ur username :")
passw = input("ur password :")
passw2 = input("rewrite ur pass: ")
mail = input("ur email : ")

while True :
    if passw == passw2 and len(passw) >8 and passw.isalpha()==False and passw.isdigit()==False :

        print("ok")
        if "@"in email:
        break
    else:
        print("again?")

