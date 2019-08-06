person = {
    "n" : "Manh",
    "age" : 16,
}
person['favs'] = ['eat','sleep']
print(person)
person['favs'].append('play')
person['favs'][1] = 'program'
print(person)
# ***********************
# print(person)
# for x in person: #person.keys()
#     print(x,person[x])
# for k in person.values():
#     print(x)
# for c,d in person.items():
#     print(c,d)
#*************

person['favs'].pop(1)
print(person)

