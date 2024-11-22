def sum_values(data_structure: list):
    """ Подсчитывает сумму элементов, переданного списка,
        (не важно, являются они ключами или значениям или ещё чем-то).
        Возвращает "0", если список пустой, иначе сумму элементов.
        Если список содержит одно число, то возвращает его.
    """
    sum_ = 0
    for elem in data_structure:
        if isinstance(elem, int | float):
            sum_ += elem
        elif isinstance(elem, str):
            sum_ += len(elem)
        else:
            if isinstance(elem, list | tuple | set):
                sum_ += sum_values(elem)
            elif isinstance(elem, dict):
                sum_ += sum_values([(k, v) for k, v in elem.items()])
    return sum_


result = sum_values([[1, 2, 3], {'a': 4, 'b': 5},
                     (6, {'cube': 7, 'drum': 8}), "Hello",
                     ((), [{(2, 'Urban', ('Urban2', 35))}])])
print(result)
