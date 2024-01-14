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

    def print_graph(self):
        for node, children in self.graph.items():
            child_list =[ child.get_name() for child in children]
            print(node.get_name(),"=>", child_list)

    def visit_node(self, node) -> str:
        print("visiting node", node.get_name())
        if not node :
            return ""
        if node.get_name() == "END":
            return node.get_name()
        for child in self.graph[node]:
            self.visit_node(child)

        return ""


    def process_nodes(self) -> str:
        res = ""
        for node in self.graph:
            if node.get_name() == "START":
                res = self.visit_node(node)
                print(res)


g = Graph()

a = Node("A")
aa = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

g.add_edge(Node("START"), a)
g.add_edge(a, b)
g.add_edge(a, c)
g.add_edge(b, d)
g.add_edge(c, d)
g.add_edge(aa, d)
g.add_edge(d, Node("END"))

g.print_graph()
# g.process_nodes()
