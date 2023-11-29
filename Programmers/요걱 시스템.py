def function(targets):
    answer = 1
    targets.sort(key = lambda x : x[0])
    #targets.sort(key = lambda x : x[1])

    s = targets[0][0]
    e = targets[0][1]
    for target in targets:
        if target[0] > s and target[1] < e:
            s = target[0]
            e = target[1]
            continue
        elif target[0] < s and target[0] < e:
            s = target[0]
            continue
        elif target[1] > s and target[1] < e:
            e = target[1]
            continue

        s = target[0]
        e = target[1]
        answer += 1
    
    return answer