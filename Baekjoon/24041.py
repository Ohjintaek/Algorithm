import sys
input = sys.stdin.readline

def getGerms(ingredients, day):
    sum_germ = 0
    for ingredient in ingredients:
        sum_germ += ingredient[0]*max(1, day - ingredient[1])
    return sum_germ
    
def getGermsAfterSorting(ingredients, day):
    sum_germ = 0
    sorted_ingredients = sorted(ingredients, key = lambda x : x[0]*max(1, day-x[1]))
    for ingredient in sorted_ingredients[:len(ingredients)-K]:
        sum_germ += ingredient[0]*max(1, day - ingredient[1])
    return sum_germ

N, G, K = map(int, input().split())
temp_ingredient = []
required_ingredient = []
for _ in range(N):
    ingredient = list(map(int, input().split()))
    if (ingredient[2] == 1):
        temp_ingredient.append(ingredient)
    else:
        required_ingredient.append(ingredient)

left, right = 0, 2*10**9
while (left <= right):
    mid = (left+right)//2
    required_germs = getGerms(required_ingredient, mid)
    if (G - required_germs >= getGermsAfterSorting(temp_ingredient, mid)):
        left = mid + 1
    else:
        right = mid - 1
print(right)