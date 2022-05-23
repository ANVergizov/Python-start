cent = "процент"
centa = "процента"
centov = "процентов"

exceptions = [11, 12, 13, 14]

for i in range(101):
    i += 1
    if i in exceptions:
        print(i, centov)
    elif i % 10 == 1:
        print(i, cent)
    elif i % 10 > 1 & i % 10 < 5:
        print(i, centa)
    else:
        print(i, centov)