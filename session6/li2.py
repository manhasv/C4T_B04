items = ['com','p','c','d']
l = len(items)
for i in range(l):
    print(items[i])
# for item in items:
    # print(item)
for i, item in enumerate(items):
    # print(i+ 1,".",item.upper())
    if 'c' in item:
        print(item)

