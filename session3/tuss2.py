import random
num = random.randint(0,100)
print(num)

if num < 30:
    print("rainy")
elif num < 60:
    print("cloudy")
else: 
    print("sunny")