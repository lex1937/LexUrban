def print_params(a=(1, 2), b='test', c=False):
    print(a, b, c)


print_params()
print_params((4, 8), '(test Ok)', True)
print_params(b='(one mod)')
print_params(b=25)  # функция вернет параметры т.к. не заданы обязательные типы
print_params(c=[1, 2, 3])  # функция вернет параметры т.к. не заданы обязательные типы

values_list = [True, 2.05, [10, 20]]
values_dict = {'a': ('test', 'Ok'), 'b': 1, 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['test', 3]
print_params(*values_list_2, 42)
