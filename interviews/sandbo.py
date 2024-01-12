from collections import defaultdict, Counter
import heapq


def process_file(filepath='/etc/words', strs=["a", "b",  "c", "c","c","b"]):


    counter = Counter(strs)

    heap = [[-count, char] for char, count in counter.items()]

    print(heap)
    heapq.heapify(heap)
    print(heap)

    while heap:
        count, char = heapq.heappop(heap)
        print(char, count)

process_file()