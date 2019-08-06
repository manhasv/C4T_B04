from random import randint
m = {
        "x":4,
        "y":4
}
while True: 
                P = {
                        "a":randint(0,3),
                        "b":randint(0,3)
                }
                K = {
                        "x":randint(0,3),
                        "y":randint(0,3)
                }
                E = {
                        "x":randint(0,3),
                        "y":randint(0,3)
                }

                if ((P['a'] != K['x']) and (P['b'] != K['y'])) and ((P['a'] != E['x']) and (P['b'] != E['y'])) and ((K['x'] != E['x']) and (K['y'] != E['y'])):
                        break
poc = 0
while True:
        


        print(P)
        print(E)
        print(K)
                
        for y in range(4):
                for x in range(4):
                                
                        if x == P['a'] and y == P['b']:
                                print("P",end=" ")
                        elif x == K['x'] and y == K['y']:
                                if poc == 0:
                                        print("K",end = " ")
                                else:
                                        print("-",end= " ")
                        elif x == E['x'] and y == E['y']:
                                        print("E",end =" ")
                        else:
                        
                                print("-",end =" ")
                print()

        move = input("a/w/s/d").lower()
        
        if move == "w":
                P["b"] -= 1
                if P["b"] < 0: 
                        P['b'] += 1
                        print("Out of move")
                print(P)
        elif move == "d":
                P["a"] += 1
                if P["b"] > 3: 
                        P['b'] -= 1
                        print("Out of move")
                print(P)
        elif move == "s":
                P["b"] += 1
                if P["b"] > 3: 
                        P['b'] -= 1
                        print("Out of move")
                print(P)
        elif move == "a":
                P["a"] -= 1
                if P["b"] < 0: 
                        P['b'] += 1
                        print("Out of move")
                print(P)
        else:
                break
        
        if P["a"] == K["x"] and P["b"] == K["y"]:
                poc = poc +1
                print("u have the key")
        if P["a"] == E["x"] and P["b"] == E["y"]:
                if poc != 0:
                        print("pass")
                else:
                        print("U need the key")

        

        # if P == K:
        #         print("U get the key")
        #         pocket = K
        # elif P == E and pocket == K:
        #         print("congratz")
        # else:
        #         print("U need the key")


# b = randint(0,4)
# c = randint(0,4)
# char = [b,c]
# print(char)
# door = [randint(0,4),randint(0,4)]
# print(door)
# key = [randint(0,4),randint(0,4)]
# print(key)
# move = input("a/w/s/d")
# if move == d:
#         c +=1
#         print(char)
# elif move == a:
#         c = b-1
#         print(char)
# elif move == s:
#         b = b
# if move in "wasd":
#     index, increment = {
#         "w": (0, -1),
#         "a": (1, -1),
#         "s": (0, 1),
#         "d": (1, 1),
#     }(move)
#     try:
#         char_xy[index] += increment
#     except IndexError:
#         print("That is not a valid move")