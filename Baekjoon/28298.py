import sys
input = sys.stdin.readline

def find_max_color(colors):
    color_set = set(colors)
    favorite_color = colors[0]
    count = 0
    for color in color_set:
        temp_count = colors.count(color)
        if (temp_count > count):
            favorite_color = color
            count = temp_count
    return favorite_color, count


N, M, K = map(int, input().split())
tiles = []
for _ in range(N):
    tiles.append(list(input().strip()))

favorite_color = []
count = 0
for i in range(K):
    for j in range(K):
        color = []
        for k in range(N//K):
            color.extend(tiles[i+K*k][j:M:K])
        max_color, max_color_count = find_max_color(color)
        favorite_color.append(max_color)
        count += (len(color) - color.count(max_color))

print(count)
for _ in range(N//K):
    for i in range(K):
        for _ in range(M//K):
            print(*favorite_color[i*K:i*K+K], sep="", end="")
        print()