class LinkedListNode:
    def __init(self,val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthNode(self, head: LinkedListNode, n: int):
        newNode = LinkedListNode(0, head)
        left = newNode
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1


        while right:
            left = left.next
            right = right.next


        left.next = left.next.next

        return newNode.next

