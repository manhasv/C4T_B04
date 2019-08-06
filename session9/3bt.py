dic ={
    "HP": 20,

    "DELL": 50,

    "MACBOOK": 12,

    "ASUS": 30
}
dic2 ={
    "HP": 600,

    "DELL": 650,

    "MACBOOK": 12000,

    "ASUS": 400
}
sum = 0
for a,b in zip(dic,dic2):
    a = dic[a]*dic2[b]
    print(a)
    sum += a
print(sum)
