my_list = list(range(1, 1001))
cube_list = []

for i in my_list:
    if i % 2 != 0:
     cube_list.append(i ** 3)

def sum_digits(value):
    res = 0

    while value != 0:
        res += value % 10
        value //= 10

    return res

res1 = 0
for i in cube_list:
    if sum_digits(i) % 7 == 0:
        res1 += i

res2 = 0
for i in cube_list:
    if sum_digits(i + 17) % 7 == 0:
        res2 += i

print(res1, res2)