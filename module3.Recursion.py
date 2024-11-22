def get_multiplied_digits(number):
    str_number = str(number)
    if str_number[-1] == '0':
        str_number = str_number[:-1]
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(4020354)
print(result)
