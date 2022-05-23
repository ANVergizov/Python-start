def_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

length = len(def_list)
i = 1

while i < length:
    def_list.insert(i, '"')
    i += 2


for i in def_list:
    print(i, end=' ')