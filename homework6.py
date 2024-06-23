# Словари и множества
my_dict = {'Aaa': 1981, 'Zzz': 1984, 'Qqq': 1981, 'Www': 1985, 'Sss': 1961, 'Xxx': 2021, }  # словарь
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Sss'))
print('Not existing value: ', my_dict.get('Ffff', 'Такой записи нет'))
my_dict.update({'Tgb': 2011, 'Yhn': 2012})  # добавить  словарь 2 элемента
print('Dictionary: ', my_dict)
date_ = my_dict.pop('Sss')  # удалить из словаря Sss
print('Deleted value: ', date_)
print('Modified dictionary: ', my_dict)
print()
my_set = {1, 2, 3, 'a1', 'a1', 'a2', 1.2, 4, 5, 5}  # множество
print('Set:          ', my_set)
my_set.add((6, 7))  # добавить кортеж
my_set.add('String1')  # добавить строку
print('Modified set: ', my_set)
my_set.discard((6, 7))  # удалить элемент, если его нет, то ошибки не будет
my_set.remove(5)  # удалить существующий элемент, если его нет, то ошибка
print('Modified set: ', my_set)
