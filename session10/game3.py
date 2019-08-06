from random import randint
m = {
        "x":4,
        "y":4
}
while True: 
                P = {   "HP":5,
                        "atk":1,
                        "def":1,
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
                mons ={
                    "HP":1,
                    "atk":2,
                    "def":0,
                    "x":randint(0,3),
                    "y":randint(0,3)
                } 

                
                if ((mons['x'] != K['x']) and (mons['y'] != K['y'])) and ((mons['x'] != E['x']) and (mons['y'] != E['y'])) and ((mons['x'] != E['x']) and (mons['y'] != E['y'])) and ((P['a'] != mons['x']) and (P['b'] != mons['y'])):
                        break
print("U",P)
poc = 0
w = {
    "x":1,
    "y":1
}
print("mons:",mons)
while True:
        # print(E)
        # print(K)
                
        for y in range(m["y"]):
                for x in range(m["x"]):
                                
                        if x == P['a'] and y == P['b']:
                                print("P",end=" ")
                        elif x == w['x'] and y == w['y']:
                                print("W", end =" ")
                        elif x == mons['x'] and y == mons['y']:
                            print("M",end =" ")
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

        move = input("a/w/s/d ").lower()
        
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
            
        if P['a'] == mons['x'] and P['b'] == mons['y']:
            while True:
                dam = mons['atk'] - P['def']
                dam2 = P['atk'] - mons['def']
                move = input("run or combat? ")
                rate1 = randint(0,10)
                rate2 = randint(0,10)
                print("hit rate:",rate2)
                if move == 'run':
                    if rate1 > 5:
                        break
                    else:
                        print("can't run away")
                        P['HP'] -= dam
                        print("Ur HP",P['HP'])

                if move == 'combat':
                    if rate2 >5:
                        mons['HP'] -= dam2
                        print("mons's HP: ",mons['HP'])
                        if mons['HP'] < 1:
                            print("monster died")
                            break
                        else:
                            P['HP'] -= dam
                        print("U",P['HP'])
                    else:
                        P['HP'] -= dam
                        print("U",P['HP'])
                    if P['HP'] < 1:
                        print("ur dead")
                        break


        if P["a"] == K["x"] and P["b"] == K["y"]:
                poc = poc +1
                print("u have the key")
        if P["a"] == E["x"] and P["b"] == E["y"]:
                if poc != 0:
                        print("pass")
                else:
                        print("U need the key")