def thesaurus(*args):
    names = {}
    for i in args:
        key = i[0].capitalize()  # Обьявляем ключ
        if key not in names:     # Проверка на наличие уже имеющегося ключа
            names[key] = []
            names[key].append(i)
        print(names)


thesaurus('lupa','pupa')