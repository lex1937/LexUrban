calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string):
    tuple_ = tuple((len(string), string.upper(), string.lower()))
    count_calls()
    return tuple_


print(string_info('PhyTOn'))
print(string_info('lesson one'))
print(string_info('hello WORLD!'))


def is_contains(string, list_to_search):
    while True:
        bool_ = string.upper() in [u.upper() for u in list_to_search]
        count_calls()
        return bool_


print(is_contains('oleg', ['ALEXEY', 'Igor', 'LeX']))
print(is_contains('MODULE', ['function', 'conjunction', 'disjunction', \
                             'module']))
print(is_contains('AbRa', ['arba', 'abra', 'Kadabra']))
print(calls)
