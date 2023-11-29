import sys
input = sys.stdin.readline

while True:
    A = list(map(int, input().split()))
    if len(A) == 1:
        break
    B = list(map(int, input().split()))

    A = A[1:]
    B = B[1:]
    length_A = len(A)
    length_B = len(B)
    accum_A = [A[0]]
    accum_B = [B[0]]

    for i in range(1, length_A):
        accum_A.append(accum_A[i - 1] + A[i])
    
    for i in range(1, length_B):
        accum_B.append(accum_B[i - 1] + B[i])

    indexes = []
    temp_B_index = 0
    for i in range(length_A):
        if B[temp_B_index] > A[i]:
            temp_B_index += 1
            if temp_B_index == length_B:
                break
            continue
        for j in range(temp_B_index, length_B):
            if A[i] == B[j]:
                indexes.append([i, j])
                temp_B_index = j
                break
    
    answer = 0
    for i in range(len(indexes)):
        if i == 0:
            temp_max = max(accum_A[indexes[i][0]], accum_B[indexes[i][1]])
        else:
            temp_max = max(accum_A[indexes[i][0]] - accum_A[present_position[0]], accum_B[indexes[i][1]] - accum_B[present_position[1]])
        answer += temp_max
        present_position = indexes[i]
    
    if indexes:
        temp_max = max(accum_A[-1] - accum_A[present_position[0]], accum_B[-1] - accum_B[present_position[1]])
    else:
        temp_max = max(accum_A[-1], accum_B[-1])
    answer += temp_max

    print(answer)