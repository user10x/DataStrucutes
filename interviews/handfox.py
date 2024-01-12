# from collections import defaultdict, Counter
# import heapq
#
#
# def process_file(filepath='/etc/words', strs=["a", "b",  "c", "c","c","b"]):
#
#
#     counter = Counter(strs)
#
#     heap = [[-count, char] for char, count in counter.items()]
#
#     print(heap)
#     heapq.heapify(heap)
#     print(heap)
#
#     while heap:
#         count, char = heapq.heappop(heap)
#         print(char, count)
#
# process_file()


from collections import defaultdict


class Node:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.result = ""

    def add_edge(self, source: Node, destination: Node):
        self.graph[source].append(destination)

    def visit_node(self, node) -> str:
        if node.get_name() == "END":
            return node.get_name()
        for child in self.graph[node]:
            self.result + self.visit_node(child)

    def process_nodes(self) -> str:
        res = ""
        for k, v in self.graph.items():
            if k.get_name() == "START":
                res = self.visit_node(k)


g = Graph()

g.add_edge(Node("A"), Node("B"))
g.add_edge(Node("A"), Node("B"))
g.add_edge(Node("A"), Node("C"))
g.add_edge(Node("B"), Node("C"))
g.add_edge(Node("C"), Node("A"))
g.add_edge(Node("C"), Node("D"))
g.add_edge(Node("D"), Node("D"))

g.process_nodes()
