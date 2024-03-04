import heapq

_list = [32,16,54,94,81,31]
heapq.heapify(_list)

heapq.heappush(_list, 7)
print(heapq.heappop(_list))

print(heapq.heappushpop(_list, 100))

small_element = heapq.nsmallest(4, _list)
print(small_element)

large_element = heapq.nlargest(4, _list)
print(large_element)