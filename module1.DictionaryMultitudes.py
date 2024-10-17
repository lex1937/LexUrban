my_dict = {'Yra': 1980, 'Maxim': 1975}
print(my_dict)
print(my_dict.get("Maxim"))
print(my_dict.get("Aleksey"))
my_dict.update({'Alexey': 1985, 'Ruslan': 1990})
print(my_dict.pop('Yra'))
print(my_dict)
my_set = {10, 20, False, 20, 35, 'Alexey', 15.8}
print(my_set)
my_set.update(['Maxim', (1, 3)])
my_set.pop()
print(my_set)