from sys import argv

class Node(object):
    def __init__(self, data = None, next = None):
        self.__data = data
        self.__next = next

    def setData(self, data):
        # Set the "data" data field to the corresponding input
        self.__data = data


    def setNext(self, next):
        # Set the "next" data field to the corresponding input
        self.__next = next

    def getData(self):
        # Return the "data" data field
        return self.__data


    def getNext(self):
        # return the "next" data field
        return self.__next

class Queue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self, newData):
        # Create a new node whose data is newData and whose next node is null
        # Update head and tail
        # Hint: Think about what's different for the first node added to the Queue
        node = Node(newData, None)
        if self.isEmpty() == 1:
            self.__tail = node
            self.__head = node
        else:
            self.__tail.setNext(node)
            self.__tail = node

    def dequeue(self):
        #  Return the head of the Queue
        #  Update head
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        if self.isEmpty() == 1:
            return None
        else:
            temp = self.__head.getData()
            self.__head = self.__head.getNext()
            return temp

    def isEmpty(self):
        # Check if the Queue is empty
        if self.__head == None:
            if self.__tail == None:
                return 1
        else:
            return 0

    #def printQueue(self):
        # Loop through your queue and print each Node's data
        #while(self.__head != None):
            #front = self.__head.getData()
            #print(front)

class Stack(object):
    def __init__(self):
        # We want to initialize our Stack to be empty
        # (ie) Set top as null

        self.__top = None


    def push(self, newData):
        # We want to create a node whose data is newData and next node is top
        # Push this new node onto the stack
        # Update top
        if self.isEmpty() == 1:
            node = Node(newData)
        else:
            node = Node(newData, self.__top)
            self.__top = node

    def pop(self):
        # Return the Node that currently represents the top of the stack
        # Update top
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        if self.isEmpty() == 1:
            return None
        else:
            temp = self.__top.getData()
            self.__top = self.__top.getNext()
            return temp


    def isEmpty(self):
        # Check if the Stack is empty
        if (self.__top == 0):
            return 1
        else:
            return 0

    #def printStack(self):
        # Loop through your stack and print each Node's data
        #newData = None
        #node = Node(newData, None)
        #while (self.isEmpty() == 1):
            #print(node.getData())

def main(argv):
    # Create a Scanner that reads system input
    input_file = argv[1]
    # Loop over the scanner's input
    with open(input_file, 'r') as file_ob:
        # For each line of the input, send it to isPalindrome()
        #get rid of first number
        firstnum = file_ob.readline()

        for num in file_ob:
            #get rid of unnecessary characters
            num = num.strip()
            if isPalindrome(num):
                print('This is a Palindrome.')
            else:
                print('Not a Palindrome')
            # If isPalindrome returns true, print "This is a Palindrome."
            # Otherwise print "Not a Palindrome."



def isPalindrome(s):
    # Use your Queue and Stack class to test wheather an input is a palendrome
    myStack = Stack()
    myQueue = Queue()

    #adds each number into stack and queue
    for number in s:
        myStack.push(number)
        myQueue.enqueue(number)

    #matches number while going through to see if first equals last
    for number in s:
        first = myStack.pop()
        last = myQueue.dequeue()
        if (first != last):
            return False

    return True
    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    #if True:
    #    return True:
    #else:
    #    return False:

def isPalindromeEC(s):
    # Implement if you wish to do the extra credit.
    return

if __name__ == "__main__":
    main(argv)
