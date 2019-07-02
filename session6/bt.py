items = ['com','p','c','d']
print(items)
i = input(" choose c/r/u/d : ")
if i == 'c' :
    new = input("new :")
    items.append(new)
    print(items)
elif i == 'r':
    l = len(items)
    for i in range(l):
        print(items[i])
elif i == 'u':
    i = int(input("num : "))
    replacing_item = input(" new : ")
    items[i] = replacing_item
    print(items)
else:
    i = int(input("a number? "))
    items.pop(i)
    print(items)





