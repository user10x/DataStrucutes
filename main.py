#########################################
################ Arrays #################

# reverses list of string/numbers in O(n) time, inplace
def reverse(numbers):
    start_index = 0
    end_index = len(numbers) - 1

    while start_index < end_index:
        temp = numbers[start_index]
        numbers[start_index] = numbers[end_index]
        numbers[end_index] = temp
        start_index = start_index + 1
        end_index = end_index - 1
    return numbers


# palindrome checks if a string is a palindrome or not
def is_palindrome(data):
    d = list(data)
    d = reverse(d)
    if data == "".join(d):
        return True
    return False


# reverse_integer reverses an integer and gives back an integer
def reverse_integer(value):
    reverse_int = 0
    while value >= 1:
        reverse_int = (reverse_int * 10) + value % 10
        value = value // 10
    return reverse_int


# is_anagram matches and returns if two strings an anagram
def is_anagram_arr(data1, data2):
    if len(data1) != len(data2):
        return False

    # extra space assuming all alphabets
    arr = [0] * 26

    # first pass for entering the first elment
    for i in range(len(data1)):
        idx = ord(data1[i]) - 97
        if arr[idx] != 0:
            arr[idx] += 1
        else:
            arr[idx] = 1

    for i in range(len(data2)):
        idx = ord(data2[i]) - 97
        if arr[idx] != 0:
            arr[idx] -= 1
        else:
            return False

    return True


# is_anagram_map uses an auxiliary map to do the lookup
def is_anagram_map(data1, data2):
    if len(data1) != len(data2):
        return False
    str_map = {}

    # first pass to input elements
    for ele in data1:
        if ele in str_map:
            str_map[ele] += 1
        else:
            str_map[ele] = 1

    # second pass find the number of elements is equal to the map elements
    for ele in data2:
        if ele in str_map:
            str_map[ele] -= 1
        else:
            return False
    return True


# is anagram sorts the strings and matches them to find if they are same
def is_anagram_sort(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


# finds duplicates in O(n), no extra space needed, given number will be from 0 through N, only deals with positive
# values
def has_duplicates(nums):
    print(nums)
    for num in nums:
        if nums[abs(num)] < 0:
            return False
        else:
            nums[abs(num)] = -nums[abs(num)]
    return True


#########################################
################ SinglyLinkedList #################

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # insert_start inserts at beginning the  of the linked list
    def insert_start(self, data):
        new_node = SinglyLinkedListNode(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # O(n) complexity for inserting at the end
    def insert_end(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        self.size += 1

    # removes the data
    def remove(self, data):
        if self.head is None:
            return

        current = self.head
        previous = None

        while current:
            if current.data != data:
                previous = current
                current = current.next
            else:
                self.size -= 1
                if previous is None:
                    self.head = current.next
                    return

                previous.next = current.next
                return

    # traverse finds an item if present, else -1
    def traverse(self, data):
        current = self.head
        idx = 0
        if current is None:
            return -1
        while current:
            if current.data == data:
                return idx
            current = current.next
            idx = idx + 1
        return -1

    # list_size returns size
    def list_size(self):
        return self.size

    # print the elements of the list
    def items(self):
        ele = []
        current = self.head
        while current is not None:
            ele.append(current.data)
            current = current.next
        return ele


#########################################
################ Stack ##################

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        del self.stack[-1]

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    # The aim is to design an algorithm that can return the maximum item of a stack in O(1) running time complexity. We can use O(N) extra memory!
    def max_element_from_stack(self):
        return "debug"


#########################################
############# Queue(Array) ##############

class QueueArray:
    def __init__(self):
        self.queue = []

    # returns true/false based on length
    def is_empty(self):
        return len(self.queue) == 0

    # O(1) to insert at the end of the array
    def enqueue(self, data):
        self.queue.append(data)

    # O(n) time to move the items bacj
    def dequeue(self):
        if self.is_empty():
            return -1
        del self.queue[0]

    # O(1) returns the first element
    def peek(self):
        if self.is_empty():
            return -1
        return self.queue[0]


#########################################
################ Heap(Max) ##################

class MaxHeap:
    CAPACITY = 10

    def __init__(self):
        # this is the number of items in the heap
        self.heap_size = 0
        # fills 0's for the heap
        self.heap = [0] * self.CAPACITY

    # inserts an item a the desired location
    def insert(self, item):
        # if the heap is full, return
        if self.heap_size > self.CAPACITY:
            return

        # insert the element at the end
        self.heap[self.heap_size] = item
        self.heap_size += 1

        # heapify/fixup: check the heap properites
        self.fix_up(self.heap_size - 1)

    # starting with the actual node that we inserted upto the rote node
    # we have to compare the values whether to make swap operations
    # it has O(logN) running time complexity

    def fix_up(self, index):

        parent_index = (index - 1) // 2
        # we consider all the items above till we hit the root node
        # if heap property is violated  we swap parent child
        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.fix_up(parent_index)

    # get_max returns the max item in O(1) time
    def get_max(self):
        return self.heap[0]

    # get the max element, maintains the order(heapify) of element after deletion
    # heapify: move down the element
    def poll(self):
        max_element = self.get_max()
        # swap the element at the bottom
        self.heap[0] = self.heap[self.heap_size]
        self.fix_down(0)

        return max_element

    # checks the left and right child of the heap, max of l/f swaps moves upward
    # if the parent is lesser than the child nodes, move it down until we hit the bottom
    def fix_down(self, parent_index):

        left_index = 2 * parent_index + 1
        right_index = 2 * parent_index + 2

        # index out of bounds
        if left_index > self.heap_size or self.right_index > self.heap_size:
            return

        swap_index = None
        if self.heap[left_index] > self.heap[right_index]:
            swap_index = right_index
        else:
            swap_index = left_index

        # if the element on top is lower
        # violates the heap property
        if self.heap[swap_index] > self.heap[parent_index]:
            self.heap[swap_index], self.heap[parent_index] = self.heap[parent_index], self.heap[swap_index]
            self.fix_down(swap_index)


# from collections import defaultdict
#
#
# class Graph:
#
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def dfs_walk(self, v, visited):
#         visited.add(v)
#
#         print(v, end=' ')
#         for neighbour in self.graph[v]:
#             if neighbour not in visited:
#                 self.dfs_walk(neighbour, visited)
#
#     def dfs(self, v):
#         visited = set()
#         self.dfs_walk(v, visited)
#
#
# class GraphConnectedComponents:
#     def __init__(self, v):
#         self.v = v
#         self.adj = [[] for i in range(v)]
#
#     # undirectec edge
#     def add_edge(self, u, v):
#         self.adj[u].append(v)
#         self.adj[v].append(v)
#
#     # connected componets
#     def connected_components(self):
#         visited = []
#         cc = []
#         for i in range(self.v):
#             visited.append(False)
#         for v in range(self.v):
#             if not visited[v]:
#                 temp = []
#                 self.dfs_util(temp, v, visited)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # arrays
    print(reverse([1, 2, 3]))

    print(is_palindrome("madam"))
    print(is_palindrome("nipun"))

    print(reverse_integer(1234))

    print(is_anagram_arr("restful", "fulrest"))
    print(is_anagram_map("restfull", "fullrest"))

    print(is_anagram_sort("one", "noz"))
    print(has_duplicates([2, 1, 2, 4, 3]))

    # linklist
    print('#' * 100)
    print('Linklist --- implementation')
    l = LinkedList()
    l.insert_start(0)
    l.insert_start(1)
    l.insert_end(4)

    print(l.items())
    print(f'value 0 index is {l.traverse(0)} ')
    print(f'value 4 index is {l.traverse(4)} ')
    print(f'list size is {l.list_size()} ')

    print(f'removing 4 from the list {l.remove(4)} ')
    print(f'list size is {l.list_size()} ')
    print(f'list items are {l.items()}')

    print(f'removing 0 from the list {l.remove(1)} ')
    print(f'list size is {l.list_size()} ')
    print(f'list items are {l.items()}')

    # doubly

    # linkedlist problems
    # stacks
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    print(stack.is_empty())
    stack.pop()
    stack.pop()
    print(stack.is_empty())
    stack.max_element_from_stack()

    # queues

    q = QueueArray()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Queues")
    print(q.peek())
    q.dequeue()
    print(q.is_empty())
    print(q.peek())
    q.dequeue()
    q.dequeue()

    # stacks/queues problems
    # trees

    # heap

    m = MaxHeap()  # maybe look into priority queue pattern in Python collections package
    m.insert(10)

    # graphs
    # g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    # print("Following is DFS from (starting from vertex 2)")
    # g.dfs(2)
    #
    # # bfs
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': ['F'],
    #     'F': []
    # }
    #
    # visited = []  # List to keep track of visited nodes.
    # queue = []  # Initialize a queue
    #
    #
    # def bfs(visited, graph, node):
    #     visited.append(node)
    #     queue.append(node)
    #
    #     while queue:
    #         s = queue.pop(0)
    #         print(s, end=" ")
    #
    #         for neighbour in graph[s]:
    #             if neighbour not in visited:
    #                 visited.append(neighbour)
    #                 queue.append(neighbour)
    #
    #
    # # Driver Code
    # bfs(visited, graph, 'A')
