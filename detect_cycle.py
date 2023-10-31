
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        temp = self.head
        while temp != Node:
            print(temp.data, end=" ")

    def detectLoop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)

            temp = temp.next

        return False

    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)

