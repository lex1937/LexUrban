result = []
key_ = int(input())
while True:
    for i in range(1, (key_ // 2) + 1):  # for i in range(1, key_):
        for j in range(i + 1, key_):  # for j in range(1, key_):
            if key_ % (i + j) == 0:  # and j > i:  # and i != j:
                result.extend([i, j])
    print((''.join(str(elem) for elem in result)))  # print(*result)
    break
