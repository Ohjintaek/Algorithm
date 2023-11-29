import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    global answer
    to_visit_hypertubes = deque()
    visited_hybertubes = [False]*M
    to_visit_stations = deque()
    visited_stations = [False]*(N+1)

    to_visit_hypertubes.extend(stations[start])

    while to_visit_hypertubes:
        temp_stations = set()
        while to_visit_hypertubes:
            hypertube = to_visit_hypertubes.pop()
            for station in hypertubes[hypertube]:
                if not visited_stations[station]:
                    temp_stations.add(station)
            visited_hybertubes[hypertube] = True
        to_visit_stations.extend(temp_stations)

        answer += 1

        temp_hypertubes = set()
        while to_visit_stations:
            station = to_visit_stations.pop()
            if station == N:
                return True
            for hypertube in stations[station]:
                if not visited_hybertubes[hypertube]:
                    temp_hypertubes.add(hypertube)
            visited_stations[station] = True
        to_visit_hypertubes.extend(temp_hypertubes)
        
    return False

N, K, M = map(int, input().split())
hypertubes = []
for _ in range(M):
    hypertubes.append(list(map(int, input().split())))

stations = [[] for _ in range(N+1)]
for i in range(M):
    for station in hypertubes[i]:
        stations[station].append(i)
answer = 1

if N == 1:
    print(1)
elif dfs(1):
    print(answer)
else:
    print(-1)
