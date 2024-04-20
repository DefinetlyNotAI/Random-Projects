import random

lowest = 1
highest = int(input("How man dice sides? "))

while True:
    dieNo = int(input("How many dices? "))
    for i in range(dieNo):
        print(random.randint(lowest, highest))