numberList = [1, 2, 3]
numberList2 = [7, 8, 9]
strList = ['one', 'two', 'three']

for a,b,c in zip(numberList,strList,numberList2):
    print(a," * ",b," * ",c)