'''
employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []
for i in employees:
    names.append(i.split(' ', -1)[-1])
for el in names:
    el = el.capitalize()
    print(f'Hello ', el,'!')
print(names)
'''

employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in employees:
    print(f'Hello ',i.split(' ', -1)[-1].capitalize(), '!')