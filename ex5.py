from random import choices
from random import sample

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

uniq_func = {True: sample, False: choices}

def get_jokes(n, uniq):
    ansv =[]
    if n > min([len(nouns), len(adverbs), len(adjectives)]):
        return 'Много для вас шуток'
    _nouns = uniq_func[uniq](nouns, k=n)
    _adverbs = uniq_func[uniq](adverbs, k=n)
    _adjectives = uniq_func[uniq](adjectives, k=n)
    for noun, adverb, adjective in zip(_nouns, _adverbs, _adjectives):
        ansv = ' '.join([noun, adverb, adjective])
        return ansv

jokes = []
user_jokes = input('Сколько шуток вы жилаете? ')
if user_jokes.isdigit() and int(user_jokes):
    only = input('Введите что нибудь: ')
    jokes = get_jokes(n=int(user_jokes), uniq=bool(only))
else:
    jokes = 'Что-то не до шуток...'

print(jokes)


