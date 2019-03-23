

class Node:

    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None



class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def listLength(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getNext()
            count = count + 1
        return count

    def size(self):
        return self.length

    def insertInFront(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

        self.length = self.length +1
        return


    # 1 2 3
    # 1 2 (a) 3
    # 2 5 10
    #
    def insertAtPost(self, data, pos):
        if pos > self.length:
            return "position out of bound"
        current = self.head
        previous = None
        while pos > 0:
            previous = current
            current = current.getNext()
            pos -= 1

        new_node = Node()
        new_node.setData(data)
        new_node.setNext(current)
        previous.setNext(new_node)
        self.length += 1


    def insertAtEnd(self,data):
        if self.length == 0:
            return
        current = self.head
        while current.getNext():
            current = current.getNext()

        newNode = Node()
        newNode.setData(data)
        current.setNext(newNode)
        current.setNext
        self.length +=1

        return

    def deleteFromFront(self,data):
        if self.length == 0:
            return
        if self.head.getData() == data:
            self.head = self.head.getNext()
            self.length -= 1

    def deleteFromEnd(self,data):

        return

    def traverse(self):
        current = self.head
        while current != None:
            print('traversing through ' + str(current.getData()))
            current = current.getNext()




if __name__ == '__main__':
    newList = LinkedList()
    newList.insertInFront(10)
    newList.insertInFront(5)
    newList.insertInFront(2)
    newList.insertInFront(1)
    print ('size of the list 1)  ' + str(newList.listLength()))

    newList.insertAtPost(7,pos=2)
    newList.insertAtPost(11,pos=5)
    newList.insertAtEnd(12)
    print ('size of the list 2) ' + str(newList.listLength()))


    print ('size of the list 3) ' + str(newList.size()))
    print(newList.traverse())


    newList.deleteFromFront(1)
    print ('size of the list 4) ' + str(newList.size()))

    print(newList.traverse())

