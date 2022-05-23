from random import random, randint
numbs = []
while len(numbs) != 20:
    numbs.append(randint(1, 100) + random())

numbs.sort()
for numb in numbs:
    rub = int(numb)
    kop = (numb - int(numb)) * 100
    print(f'{rub}руб. {kop:02.0f}коп.')