

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

    def insertAtPost(self, data, pos):
        if pos > self.length:
            return "postion out of bound"
        current = self.head

        while pos > 0:
            print(current)
            current = current.getNext()
            pos = pos - 1

        newNode = Node()
        newNode.setData(data)
        temp = current.getNext()
        newNode.setNext(temp)


    def insertAtEnd(self,data):
        return

    def deleteFromFront(self,data):
        return

    def deleteFromEnd(self,data):
        return

    def traverse(self):
        current = self.head
        while current != None:
            print('traversing through ' + str(current.getData()))
            current = current.getNext()
        return




if __name__ == '__main__':
    newList = LinkedList()
    newList.insertInFront(10)
    newList.insertInFront(5)
    newList.insertInFront(2)
    newList.insertAtPost(7,pos=2)


    print ('size of the list ' + str(newList.listLength()))
    print(newList.traverse())
