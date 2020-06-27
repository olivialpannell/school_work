
# BinarySearchTree is a class for a binary search tree (BST)
# when called, a BST is initialized with no root and size 0.
# size keeps track of the number of nodes in the tree
from Node import RB_Node



class RedBlackTree:
    # initialize root and size
    def __init__(self):
        self.root = None
        self.size = 0
        self.sentinel = RB_Node(None,None, color = 'black')
        self.__pretty = False
        self.sentinel.parent = self.sentinel
        self.sentinel.leftChild = self.sentinel
        self.sentinel.rightChild = self.sentinel

    '''
    Free Methods
    '''

    def sentinel(self):     
        return self.sentinel

    def __iter__(self):
        # in-order iterator for your tree
        return self.root.__iter__()

    def getKey(self, key):
        # expects a key
        # returns the key if the node is found, or else raises a KeyError

        if self.root:
            # use helper function _get to find the node with the key
            res = self._get(key, self.root)
            if res: # if res is found return the key
                return res.key
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    
    def getNode(self, key):
        # expects a key
        # returns the RB_Node object for the given key
        
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function _get receives a key and a node. Returns the node with
    # the given key
    def _get(self, key, currentNode):
        if currentNode is self.sentinel: # if currentNode does not exist return None
            #print("couldnt find key: {}".format(key))
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            # recursively call _get with key and currentNode's leftChild
            return self._get( key, currentNode.leftChild )
        else: # key is greater than currentNode.key
            # recursively call _get with key and currentNode's rightChild
            return self._get( key, currentNode.rightChild )

    
    def __contains__(self, key):
        # overloads the 'in' operator, allowing commands like
        # if 22 in rb_tree:
        # ... print('22 found')

        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        # Same as binary tree delete, except we call rb_delete fixup at the end.

        z = self.getNode(key)
        if z.leftChild is self.sentinel or z.rightChild is self.sentinel:
            y = z
        else:
            y = z.findSuccessor()
        
        if y.leftChild is not self.sentinel:
            x = y.leftChild
        else:
            x = y.rightChild
        
        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.leftChild:
                y.parent.leftChild = x
            else:
                y.parent.rightChild = x
        
        if y is not z:
            z.key = y.key
    
        if y.color == 'black':
            if x is self.sentinel:
                self._rb_Delete_Fixup(y)
            else:
                self._rb_Delete_Fixup(x)
        
    # pretty way of printing that'll show the colors
    # to use switch the variable __pretty to true in the init
    def pretty_print(self, n): 
        if self.__pretty:
            if n.color == 'red':
                print('\033[1;31m{}'.format(n.key)),
            else:
                print('\033[1;37m{}'.format(n.key)),
        else:
            print(n.key),


    # calling walk which will traverse
    def traverse(self, order = "in-order"):
        self.__walk(order, self.root)
        print('\033[m\n'),

    def __walk(self, order, top):
        if top is not self.sentinel :
            if order == "in-order":
                self.__walk(order, top = top.leftChild)
                self.pretty_print(top)
                self.__walk(order, top = top.rightChild)

            if order == "pre-order":
                self.pretty_print(top)
                self.__walk(order, top = top.leftChild)
                self.__walk(order, top = top.rightChild)

            if order == "post-order":
                self.__walk(order, top = top.leftChild)
                self.__walk(order, top = top.rightChild)
                self.pretty_print(top)

    '''
    Required Methods Begin Here
    '''

    #function that creates a node
    def __newNode(self, key, value):
        return RB_Node(key = key, left = self.sentinel, right = self.sentinel, parent = self.sentinel)

    def insert(self, key, value = None):
        #if the tree is empty, create the root
        if self.root == None:
            self.root = self.__newNode(key, value)
            self.root.color = 'black'
            return

        #else insert node into tree and call fixup
        x = None
        temp = self.root
        while temp != self.sentinel:
            x = temp
            if key == temp.key:
                return 0
            if key > temp.key:
                temp = temp.rightChild                
            else:
                temp = temp.leftChild
        temp = self.__newNode(key, value)
        if key > x.key:
            x.rightChild = temp
        else:
            x.leftChild = temp
        temp.parent = x
        self._rbInsertFixup(temp)
        return

    def _rbInsertFixup(self, z):
        #fixes the colors and does any changes if needed
        while z.parent.color == 'red':
            if z.parent.key == z.parent.parent.leftChild.key:
                y = z.parent.parent.rightChild
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.rightChild:
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.leftChild
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.leftChild:
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.leftRotate(z.parent.parent)

        self.root.color = 'black'


    def _rb_Delete_Fixup(self, x):
        # receives a node, x, and fixes up the tree, balancing from x.
        while x != self.root and x.color == 'black':
            if x.key == x.parent.leftChild.key:
                w = x.parent.rightChild
                if w.key == None:
                    break
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.leftRotate(x.parent)
                    w = x.parent.rightChild
                if w.leftChild.color == 'black' and w.rightChild.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.rightChild.color == 'black':
                        w.leftChild.color = 'black'
                        w.color = 'red'
                        self.rightRotate(w)
                        w = x.parent.rightChild
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.rightChild.color = 'black'
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.leftChild
                if w.key == None:
                    break
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rightRotate(x.parent)
                    w = x.parent.leftChild
                if w.rightChild.color == 'black' and w.leftChild.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.leftChild.color == 'black':
                        w.rightChild.color = 'black'
                        w.color = 'red'
                        self.leftRotate(w)
                        w = x.parent.leftChild
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.leftChild.color = 'black'
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 'black'


    def leftRotate(self, currentNode):
        # perform a left rotation from a given node
        y = currentNode.rightChild
        currentNode.rightChild = y.leftChild
        if y.leftChild != self.sentinel:
        	y.leftChild.parent = currentNode

        y.parent = currentNode.parent
        if currentNode.parent == self.sentinel:
        	self.root = y

        elif currentNode == currentNode.parent.leftChild:
        	currentNode.parent.leftChild = y
        else:
        	currentNode.parent.rightChild = y

        y.leftChild = currentNode
        currentNode.parent = y




    def rightRotate(self, currentNode):
        # perform a right rotation from a given node
       	y = currentNode.leftChild
        currentNode.leftChild = y.rightChild
        if y.rightChild != self.sentinel:
        	y.rightChild.parent = currentNode

        y.parent = currentNode.parent
        if currentNode.parent == self.sentinel:
        	self.root = y

        elif currentNode == currentNode.parent.rightChild:
        	currentNode.parent.rightChild = y
        else:
        	currentNode.parent.leftChild = y

        y.rightChild = currentNode
        currentNode.parent = y

    #search function
    def search(self, x):
        #calls contains to see if found
        if self.__contains__(x):
            print("Found")
        else:
            print("Not Found")
