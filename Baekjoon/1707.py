import sys
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x : x[0])

    A, B = dict(), dict()
    answer = "YES"
    for edge in edges:
        u, v = edge[0], edge[1]
        if u not in A and u not in B:
            if v in A:
                B[u] = True
            elif v in B:
                A[u] = True
            else:
                A[u] = True
                B[v] = True
        elif u in A:
            if v in A:
                answer = "NO"
                break
            B[v] = True
        else:
            if v in B:
                answer = "NO"
            A[v] = True

    print(answer)