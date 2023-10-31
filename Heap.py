import heapq
from heapq import heappop,heappush, heapify

# initialize the list
l = [5, 7, 9, 1, 3]

# using the heapify to converst the list into heap
heapq.heapify(l)

# print the created heap
print(l)

# using the heappush t`o push the element into the queue
heapq.heappush(l, 4)

print(l)

print(heapq.heappop(l))


pq = [ ]
heappush(pq, (10, task1))
heappush(pq, (5, task2))
heappush(pq, (15, task3))
priority, task = heappop(pq)