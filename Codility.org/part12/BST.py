
class TreeNode:
    def __init__(self, value, p=None, l=None,r=None):
        self.l= l
        self.r= r
        self.p =p
        self.value = value



class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        if not value:
            return -1
        node = TreeNode(value)
        if not self.head:
            self.head = node
            self.size += 1
            return value
        else:
            parent_node = self.head
            while 1:
                if parent_node.value == value:
                    return -1
                elif parent_node.value > value:
                    if parent_node.l:
                        parent_node = parent_node.l
                        continue
                    else:
                        parent_node.l = node
                        self.size += 1
                        return value
                else: # parent_node.value < value:
                    if parent_node.r:
                        parent_node = parent_node.r
                        continue
                    else:
                        parent_node.r = node
                        self.size += 1
                        return value

    def delete(self):
        print "NOT IMPLEMENTED"

    def min(self):
        if not self.head:
            return -1
        else:
            parentNode = self.head
            while 1:
                if parentNode.l:
                    parentNode = parentNode.l
                    continue
                else:
                    return parentNode.value

    def __repr__(self):
        return "NOT IMPLEMENTED"

    def isValidBST(self):
        print "NOT IMPLEMENTED"
        return -1


bst= BinarySearchTree()
assert bst.add(10) == 10
assert bst.head.value == 10
assert bst.add(10) == -1
assert bst.add(5) == 5
assert bst.add(3) == 3
assert bst.add(4) == 4
assert bst.add(4) == -1
assert bst.add(12) == 12
assert bst.min() == 3
print str(bst)