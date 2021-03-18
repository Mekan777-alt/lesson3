name_list = ['Иван Сергеев', 'Петр Александрович', 'Николай Николаевич', 'Сергей Сергеевич']

def thesaurus(names):

    forname = []
    surname = []
    sum_name = []

    for name in names:
        forname.append(name.split()[0])
        surname.append(name.split()[1])
    for s, v in sorted(zip(forname, surname)):
        sum_name.append(f'{s} {v}')
    name_dict = {}
    for name in sum_name:
        forname, surname = name.split()
        if name_dict.get(surname[0]):
            if name_dict[surname[0]].get(forname[0]):
                name_dict[surname[0]][forname[0]].append(name)
            else:
                name_dict[surname[0]][forname[0]] = [name]
        else:  # если первой буквы фамилии в словаре нет
            name_dict[surname[0]] = {forname[0]: [name]}
    return name_dict

namer = thesaurus(name_list[:])
print(*namer.items(), sep='\n')
