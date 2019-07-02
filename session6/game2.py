from random import randint
from random import shuffle
while True:
    items = ['furious','madness','craziness']

    i = randint(0,len(items) - 1)
    p = items[i]
    chars = list(p)
    shuffle(chars)
    print(chars)
    guess = input("us guess : ")
    if guess == p:
        print("correct")
    else:
        print("incorrect")
        break



