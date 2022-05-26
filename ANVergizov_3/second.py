numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}


def num_translate_adv():
    num = input("Enter num - ")
    key = num.lower()
    if key in numbers:    # Проверка на наличие ключа в словаре
        value = numbers.get(key)
    else:
        return None

    if num[0] == key.capitalize()[0]:    # Проверка на регистр первой буквы
        value = value.capitalize()
    else:
        value = value
    print(value)

num_translate()