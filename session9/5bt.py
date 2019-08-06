from random import randint
skill =[
    {
    "Name": "Tackle",

    "Minimum level": 1,

    "Damage": 5,

    "Hit rate": 0.3

},
    {
    "Name": " Quick attack",

    "Minimum level":2,

    "Damage": 3,

    "Hit rate": 0.5
}
]
for i in range(len(skill)):
    print(i,skill[i]["Name"])
pl = int(input("skill num? "))
lv = int(input("lv? :"))
n = randint(1,11)
a = n* 0.1
if lv >= skill[pl]["Minimum level"] and a > skill[pl]["Hit rate"]:
    print(skill[pl]["Damage"])

else:
    print("unavailable")
