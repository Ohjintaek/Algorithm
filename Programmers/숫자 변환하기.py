x, y, n = map(int, input().split())

check_list = [-1 for i in range(y+1)]
check_list[x] = 0

for i in range(x, y):
    if (check_list[i] == -1):
        continue

    if (i*2 <= y):
        if (check_list[i*2] == -1):
            check_list[i*2] = check_list[i] + 1
        else:
            check_list[i*2] = min(check_list[i] + 1, check_list[i*2])

    if (i*3 <= y):
        if (check_list[i*3] == -1):
            check_list[i*3] = check_list[i] + 1
        else:
            check_list[i*3] = min(check_list[i] + 1, check_list[i*3])

    if (i+n <= y):
        if (check_list[i+n] == -1):
            check_list[i+n] = check_list[i] + 1
        else:
            check_list[i+n] = min(check_list[i] + 1, check_list[i+n])

print(check_list[y])
