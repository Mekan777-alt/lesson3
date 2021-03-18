# Это первая задача сделал через ветвление
def num_translate():
    while True:
        user = input('Введите число на английском: ')
        if user == 'one':
            print('один')
        elif user == 'two':
            print('два')
        elif user == 'three':
            print('три')
        elif user == 'four':
            print('четыре')
        elif user == 'five':
            print('пять')
        elif user == 'six':
            print('шесть')
        elif user == 'seven':
            print('семь')
        elif user == 'eight':
            print('восемь')
        elif user == 'nine':
            print('девять')
        elif user == 'ten':
            print('десять')
        else:
            print('None')

num_translate()

# Попробывал двумя методами, более лучше нижний вариант

numerals = {'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'
            }

def num_translate_adv(num_en):

    num_ru = numerals.get(num_en.lower())
    if not num_ru:
        return num_ru
    for i, lit in enumerate(zip(num_en, num_ru)):
        if lit[0].isupper():
            num_ru = lit[1].upper().join([num_ru[:i], num_ru[i+1:]])
    return num_ru

num = input('Введите числительное на английском: ')
print(num_translate_adv(num))
