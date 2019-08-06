name = ["H","L","M"]
sal = [0.8,1,2]
h =[10,12,20]
for a,b,c in zip(name,sal,h):
    print(a,",",b,",",c)

nhanVien = [
    {
        "Name": "Huy",
        "Role":"Waiter",
        "Hours":12,
        "SpH":0.8
    },
    {
        "Name": "Huy",
        "Role":"Waiter",
        "Hours":12,
        "SpH":0.8
    },
    {
        "Name": "Duc",
        "Role":"Waiter",
        "Hours":12,
        "SpH":0.8
    }
]
# print(nhanVien)
# Duong ={ 
#     "name" : "duong"
#     }
# nhanVien.append(Duong)
# print(nhanVien)
budget = 0
for i in range(len(nhanVien)):
    print("*"*50)
    print(nhanVien[i])
    name = nhanVien[i]["Name"]
    h = nhanVien[i]["Hours"]
    s = nhanVien[i]["SpH"]
    print(name,"co luong thang la",h*s*30)
    budget += h*s*30
    print(budget)

