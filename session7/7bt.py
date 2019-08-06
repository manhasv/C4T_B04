numberList = [10, 333, -22]
strList = ['bd', 'tl', 'eee']

maxv = max(numberList)
index = 0
for i in range(len(numberList)):
    if numberList[i] == maxv:
        index = i
print(maxv, strList[index])

minv = min(numberList)
index2 = 0
for a in range(len(numberList)):
    if numberList[a] == minv:
        index2 = a 
print(minv,strList[index2])