correct = 0
print("How many legs an octopus has:")
ans1 = {
    1:"One leg",
    2:"Four legs",
    3:"Eight legs"
}
print(ans1)
guess = int(input("ur guess : "))
if guess == 3:
    print("correct")
    correct += 1
else:
    print("incorrcect")
print("U r? :")
ans2 = {
    1:"boring",
    2:"a disgrace",
    3:"great"
}
print(ans2)
guess = int(input("ur guess : "))
if guess == 2:
    print("correct")
    correct += 1
else:
    print("incorrcect")
print("U r:")
ans3 = {
    1:"creepy",
    2:"a moron",
    3:"disgusting"
}
print(ans3)
guess = int(input("ur guess : "))
if guess == 3 or guess ==2 or guess ==1:
    print("correct")
    correct += 1
else:
    print("incorrcect")
print(correct)
