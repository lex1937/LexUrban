from math import inf


def divide(first: int | float, second: int | float):
    """ Проверка деления на '0'.
        Число first делим на число second.
        Возвращаем "Ошибка", если число second равно 0,
        иначе возвращаем результат операции.
    """

    # print("Ошибка" if second == 0 else first / second)

    try:
        first / second
    except ZeroDivisionError:
        return "Ошибка"
    else:
        return first / second
