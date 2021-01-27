class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if data < node.data:
            if node.leftchild:
                self.insertNode(data, node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertNode(data, node.rightchild)
            else:
                node.rightchild = Node(data)

    def removeNode(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.leftchild = self.removeNode(data, node.leftchild)
        elif data > node.data:
            node.rightchild = self.removeNode(data, node.rightchild)
        else:

            if not node.rightchild and not node.leftchild:
                print("Removing a leaf node")
                del node
                return None

            if not node.leftchild:
                print("Removing a node with single right child")
                tempNode = node.rightchild
                del node
                return tempNode
            elif not node.rightchild:
                print("Removing a node with single left child")
                tempNode = node.leftchild
                del node
                return tempNode

            print('Removing node with two children')
            tempNode = self.getPredecessor(node.leftchild)
            node.data = tempNode.data
            node.leftchild = self.removeNode(tempNode.data, node.leftchild)
        return node

    def getPredecessor(self, node):

        if node.rightchild:
            return self.getPredecessor(node.rightchild)

        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):

        if node.leftchild:
            return self.getMin(node.leftchild)

        return node.data

    def getMaxValue(self):

        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightchild:
            return self.getMax(node.rightchild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):

        if node.leftchild:
            self.traverseInOrder(node.leftchild)

        print("%s" % node.data)

        if node.rightchild:
            self.traverseInOrder(node.rightchild)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(12)
bst.insert(5)
bst.insert(1)
bst.remove(10)

# print(bst.getMaxValue())
# print(bst.getMinValue())
bst.traverse()
