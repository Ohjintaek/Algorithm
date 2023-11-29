def solution(name):
    answer = 0
    alpha = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}
    
    name_length = len(name)
    min_move = name_length - 1
    
    for i in range(name_length):
        answer += alpha[name[i]]

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        min_move = min([min_move, 2*i + len(name) - next, i + 2*(len(name) - next)])
                
    answer += min_move
    return answer

print(solution(input().strip()))