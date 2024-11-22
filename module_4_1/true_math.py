from math import inf


def divide(first: int | float, second: int | float):
    """ Проверка деления на '0'.
        Число first делим на число second.
        Возвращаем бесконечность(inf), если число second равно 0,
        иначе возвращаем результат операции.
    """

    # print(float('Бесконечность') if second == 0 else first / second)

    try:
        first / second
    except ZeroDivisionError:
        return inf
    else:
        return first / second
