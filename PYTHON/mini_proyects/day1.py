import heapq

li = [11,2,5,1]
heapq.heapify(li)
print(li)

heapq.heappush(li,4)
print(li)

heapq.heappop(li)
print(li)

heapq.heapreplace(li,20)
print(li)