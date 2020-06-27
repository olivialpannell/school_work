from Node import Node

class BST(object):
    def __init__(self):
        self.__root = None

    def getRoot(self):
        # Private Method, can only be used inside of BST.
        return self.__root

    def __findNode(self, data):
        # Private Method, can only be used inside of BST.
        # Search tree for a node whose data field is equal to data.
        # Return the Node object

        if self.__root == None:
            return None
        # If the root is the data
        if self.__root.getData() == data:
            return self.__root

        # If the data is less than current
        # then go right
        if self.__root.getData() < data:
            return self.__findNode(self.__root.getRightChild, data)

        #otherwise its to the left
        return self.__findNode(self.__root.getLeftChild, data)


    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        if self.__findNode(self, data) == None:
            return False
        return True

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error

        datanode = Node(data)
        if self.__root == None:
            self.__root = datanode
            return


        newnode = None
        temp = self.__root
        while temp != None:
            newnode = temp
            if datanode.getData() < temp.getData():
                temp = temp.getLeftChild()
            else:
                temp = temp.getRightChild()

        datanode.setParent(newnode)
        if newnode.getData() == None:
            self.__root = datanode
        elif datanode.getData() < newnode.getData():
            newnode.setLeftChild(datanode)
        else:
            newnode.setRightChild(datanode)
        temp = datanode

    #got this from the book and successor
    def __transplant(self, u, v):
        if u.getParent() == None:
            self.__root = v

        elif u.getData() == u.getParent().getLeftChild().getData():
            u.getParent().setLeftChild(v)

        else:
            u.getParent().setRightChild(v)

        if v != None:
            if v.getParent() == None:
                v.setParent(u.getParent())

    def __findSuccessor(self, aNode):

        if aNode == None:
            return None

        if aNode.getRightChild() == None and aNode.getLeftChild() == None:
            return None

        if aNode.getRightChild() == None:
            tmp = aNode.getLeftChild()
            while tmp.getRightChild() != None:
                tmp = tmp.getRightChild()
            return tmp

        tmp = aNode.getRightChild()
        while tmp.getLeftChild() != None:
            tmp = tmp.getLeftChild()
        return tmp


    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree.
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Hint: you may want to write a new method, findSuccessor() to find the successor when there are two children

        theNode = self.__findNode(data)
        if theNode.getLeftChild() == None:
            self.__transplant(theNode, theNode.getRightChild())
        elif theNode.getRightChild() == None:
            self.__transplant(theNode, theNode.getLeftChild())
        else:
            mini = self.__findSuccessor(theNode)

            if mini.getParent().getData() != theNode.getData():
                self.__transplant(mini, mini.getRightChild())
                mini.setRightChild(theNode.getRightChild())
                mini.getRightChild().setParent(mini)
            self.__transplant(theNode, mini)
            mini.setLeftChild(theNode.getLeftChild())
            if mini.getLeftChild() != None:
                mini.getLeftChild().setParent(mini)


        return None

    def __findmin(self, aNode):
        while aNode.getLeftChild() != None:
            aNode = aNode.getLeftChild()
        return aNode


    def traverse(self, order, top):
        # traverse the tree by printing out the node data for all node in a specified order

        if top != None:
            if order == "preorder":
                #print root, left, then right
                print(top.getData())
                self.traverse(order, top.getLeftChild())
                self.traverse(order, top.getRightChild())

            elif order == "inorder":
                #print left, root, and then right
                self.traverse(order, top.getLeftChild())
                print(top.getData())
                self.traverse(order, top.getRightChild())


            elif order == "postorder":
                #print left, right, then root
                self.traverse(order, top.getLeftChild())
                self.traverse(order, top.getRightChild())
                print(top.getData())

            else:
                print("Error, order {} undefined".format(order))
