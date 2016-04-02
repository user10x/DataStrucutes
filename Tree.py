__author__ = 'nipunchawla'

class Tree:

    def __init__(self,cargo,left=None, right=None):
        self.cargo=cargo
        self.left=left
        self.right=right

    def __str__(self):
        return self.cargo




def total(tree):
    #sum the tree nodes
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

def printTree(tree,order):
    if order=="pre":
        if tree==None: return
        print tree.cargo,
        printTree(tree.left,order)
        printTree(tree.right,order)
    if order=="post":
        if tree==None:return
        printTree(tree.left,order)
        printTree(tree.right,order)
        print tree.cargo,
    if order=="inorder":
        if tree==None:return
        printTree(tree.left,order)
        print tree.cargo,
        printTree(tree.right,order)



if __name__ == '__main__':
    left = Tree(2)
    right = Tree(3)
    root= Tree(1,left,right)
    ret=total(root)
    print ret
    tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
    printTree(tree,"pre")
    print
    printTree(tree,"post")
    print
    printTree(tree,"inorder")





