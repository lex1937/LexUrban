grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = sorted(students)
#list_students = list(students)
#list_students.sort()
aver_sc = [int(sum(grades[0])) / len(grades[0])], \
            [int(sum(grades[1])) / len(grades[1])], \
                [int(sum(grades[2])) / len(grades[2])], \
                    [int(sum(grades[3])) / len(grades[3])], \
                        [int(sum(grades[4])) / len(grades[4])]
stud_aver_sc = {list_students[0]: aver_sc[0], \
            list_students[1]: aver_sc[1], \
                list_students[2]: aver_sc[2], \
                    list_students[3]: aver_sc[3], \
                        list_students[4]: aver_sc[4]}
print(stud_aver_sc)