person = {
    "n" : "Manh",
    "age" : 16,
}
print(person)
# print(person == {})
person["status"] = input("stt: ")
print(person)
person["age"] +=1
print(person)
de = input("del :")
del person[de]
print(person)
print("name " in person == {})
