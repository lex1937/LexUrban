immutable_var = 10, 10.5, False, "lesson"
print(immutable_var)
mutable_list = [10, 10.5, False, 'lesson']
mutable_list[0] = 11
mutable_list[1] = mutable_list[1] + 0.5
mutable_list[3] = "lesson_tuple"
print(mutable_list)