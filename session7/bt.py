items = ['com','p','c','d']
l = len(items)
for i in range(l):
    print(items[i])

dele = input("delete? : ")
if dele.isdigit():
    items.pop(int(dele))

else:
    items.remove(dele)
print(items)
