import heapq
from collections import defaultdict

# Create a defaultdict with a list (heap) as the default value
heap_dict = defaultdict(list)

# Add elements to the defaultdict
heap_dict['group1'].append(3)
heap_dict['group1'].append(1)
heap_dict['group1'].append(4)
heap_dict['group2'].append(2)
heap_dict['group2'].append(6)
heap_dict['group3'].append(5)

print(heap_dict)
# Use heapq methods to manipulate the heaps
heapq.heappush(heap_dict['group1'], 5)
print(heap_dict)

heapq.heappop(heap_dict['group1'])

# Print the defaultdict
print(heap_dict)
