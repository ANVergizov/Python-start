from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    count = 1
    while count <= n:
        print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        count += 1

get_jokes(3)