from random import randint
m = {
        "x":4,
        "y":4
}
while True: 
                P = {
                        "a":0,
                        "b":0
                }
                K = {
                        "x":2,
                        "y":1
                }
                E = {
                        "x":3,
                        "y":3
                }

                if ((P['a'] != K['x']) and (P['b'] != K['y'])) and ((P['a'] != E['x']) and (P['b'] != E['y'])) and ((K['x'] != E['x']) and (K['y'] != E['y'])):
                        break
poc = 0
w = {
        "x":1,
        "y":1
}
print(P)
while True:

        
        # print(E)
        # print(K)
                
        for y in range(m["y"]):
                for x in range(m["x"]):
                                
                        if x == P['a'] and y == P['b']:
                                print("P",end=" ")
                        elif x == w['x'] and y == w['y']:
                                print("W", end =" ")
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
                if P['a'] == w['x'] and P['b'] == w['y']:
                        P['b'] +=1
                print(P)
        elif move == "d":
                P["a"] += 1
                if P["b"] > 3: 
                        P['b'] -= 1
                        print("Out of move")
                if P['a'] == w['x'] and P['b'] == w['y']:
                        P['a'] -=1
                print(P)
        elif move == "s":
                P["b"] += 1
                if P["b"] > 3: 
                        P['b'] -= 1
                        print("Out of move")
                if P['a'] == w['x'] and P['b'] == w['y']:
                        P['b'] -=1
                print(P)
        elif move == "a":
                P["a"] -= 1
                if P["b"] < 0: 
                        P['b'] += 1
                        print("Out of move")
                if P['a'] == w['x'] and P['b'] == w['y']:
                        P['a'] +=1
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