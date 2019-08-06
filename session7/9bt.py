numberList = [10, 333, 22 , 48]
# for i in range(len(numberList) ):
    
#     print(numberList[i])
# new = int(input("new :"))
# numberList.append(new)
# for i in range(len(numberList) ):
#     print(numberList[i])
new1 = sorted(numberList, reverse = True)
for i in range(len(new1)):
    print(new1[i])
new = int(input("new :"))
new1.append(new)
new2 = sorted(new1, reverse = True)
for i in range(len(new2)):
    print(new2[i])

