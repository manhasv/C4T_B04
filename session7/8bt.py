numberList = [6, 4, 9]
numberList2 = [1, 2, 3]
strList = ['one', 'two', 'three']
result = [x/y for x,y in zip(numberList,numberList2)]
print(result)
for a,b in zip(result,strList):
    print(a," * ",b)
c = sum(result)
d = len(strList)
# print(d)
ave = c / d
print(ave)
