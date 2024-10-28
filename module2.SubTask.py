result = []
key_ = int(input())
while True:
    for i in range(1, key_):
        for j in range(1, key_):
            if key_ % (i + j) == 0 and j > i:  # and i != j:
                result.extend([i, j])
    print(*result)
    break
