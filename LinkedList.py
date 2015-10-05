__author__ = 'nichawla'

"""Singly Linked List"""
# {HEAD}--->[ELEMENT_ONE]---->[ELEMENT_TWO]---->......

class Node(object):

    """Initilize the first Node"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    """Helper Functions"""
    def get_data(self):
        return self.data

    def get_next(self):
        return  self.next_node

    def set_next(self,new_next):
        self.next_node=new_next

class LinkedList(object):

    """Intiialse the head of the linked list"""
    def __init__(self,head=None,tail=None):
        self.head=head

    """Helper Functions"""
    def insert(self,data):
        """Inserts Data in front of the List"""
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node

    def size(self):
        current=self.head
        count=0
        while current:
            count=count+1
            current=current.get_next()
        return count

    def search(self,data):
        current=self.head
        found=False
        index=0
        while current is not None:
            if data==current.get_data():
                print(data+" found at index "+str(index))
                return current
            elif current is not None:
              index=index+1
              current=current.get_next()
            else:
                print("Element does not exist")

    def delete(self,data):
        current=self.head
        found=False
        previous=None
        while current is not None:
            if data==current.get_data():
                found=True
                current=current.get_next()
                previous.set_next(current)
                return found
            else:
                previous=current
                print("asdhda",previous.get_data())
                current=current.get_next()

l1=LinkedList()
l1.insert("FirstElements")
l1.insert("ExtraElement")
l1.insert(33)
l1.insert(10)
l1.insert(2000)
l1.insert(20)
l1.insert("LastElement")
print("Size of the list before")+l1.size()
l1.delete("ExtraElement")
print("Size of the list after")+l1.size()




