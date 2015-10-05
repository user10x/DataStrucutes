__author__ = 'nichawla'


# class Node(object):
#
#     def __init__(self,data=None,next_node=None):
#         self.data=data
#         self.n

    # itemOne=None
    # itemTwo="SecondElement"



# print "----"
# n=Node()
# print type(n.itemOne)
# print "-----"
# print type(n.itemTwo)

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return  self.next_node
    def self(self):
        return self.next_node

n1=Node(data=10,next_node=50)

print n1.data