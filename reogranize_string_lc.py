import heapq
from collections import Counter


def rearrange_string(s):
    counter = Counter(s)

    heap = [[-count, character] for character, count in counter.items()]
    heapq.heapify(heap)

    result = ""
    previous = None
    while len(heap) != 0:

        count, element = heapq.heappop(heap)
        result += element
        if previous == element:
            return ''

        count += 1
        if count != 0:
            heapq.heappush(heap, [count, element])
        previous = element

        print(result)
    return result



def rearrange_string2(s):
    counter = Counter(s)

    max_heap = [[-count, character] for character, count in counter.items()]
    heapq.heapify(max_heap)

    result = ""
    previous = None
    while max_heap or previous:
        if previous and not max_heap:
            return ""
        count, element = heapq.heappop(max_heap)
        result += element
        count += 1

        if previous:
            heapq.heappush(max_heap, [count, element])
            previous = None

        if count != 0:
            previous = [count, element]

    return result



print(rearrange_string("abcad"))
#print(rearrange_string2("abca"))

# print(min_heap.pop())
# print(min_heap.pop())
