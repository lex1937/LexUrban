my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind_my_list = 0
while ind_my_list < len(my_list):
    if my_list[ind_my_list] < 0:
        break
    else:
        if my_list[ind_my_list] == 0:
            ind_my_list += 1
    print(my_list[ind_my_list])
    ind_my_list += 1