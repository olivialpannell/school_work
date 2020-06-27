class MaxHeap(object):

    def __init__(self, size):
        # finish the constructor, given the following class data fields:
        self.__maxSize = size
        self.__length = 0
        self.__heap = [None] * (size + 1)

	''' free helper functions '''
    def getHeap(self):
        return self.__heap

    def getMaxSize(self):
        return self.__maxSize

    def setMaxSize(self, ms):
        self.__maxSize = ms
        # May need to add more code here if you want to use this method

    def getLength(self):
        return self.__length

    def setLength(self, l):
        self.__length = l

    def __getParent(self, i):
        if i == 1:
            return 1
        return i // 2
        
    def __getLeft(self, i):
        return 2 * i

    def __getRight(self, i):
        return (2 * i) + 1

    def __swap(self, i, j):
        temp = self.__heap[i]
        self.__heap[i] = self.__heap[j]
        self.__heap[j] = temp

    ''' Required Methods '''
    def insert(self, data):
    	# Insert an element into your heap.
        #increase length
        self.__length += 1
        if self.__length > self.__maxSize:
            return

        #set new leaf to data
        self.__heap[self.__length] = data

        # reshaping the heap after inserting an element in it
        cur = self.__length
        par = self.__getParent(self.__length)
        while cur > 1:
            if self.__heap[cur] > self.__heap[par]:
                self.__swap(cur, par)
                cur = par
                par = self.__getParent(cur)
            else:
                break

    def maximum(self):
        # return the max value in the heap
        return self.__heap[1]

    def extractMax(self):
        # remove and return the maximum value in the heap
        if self.__length < 1:
            return 0

        #set max in a temp and delete it
        maximum = self.__heap[1]
        self.__heap[1] = self.__heap[self.__length]
        self.__heap[self.__length] = None
        self.__length -= 1

        #reheapify the heap without the max
        self.__heapify(1)
        return maximum


    def __heapify(self, node):
    	# helper function for reshaping the array
        # iteratively checking to see if the children are greater than the current node
        # if so, swapping them
        while node < self.__length:
            #find left and right index for node
            left = self.__getLeft(node)
            right = self.__getRight(node)

            largest = left
            if right < self.__length:
                if self.__heap[right] > self.__heap[left]:
                    largest = right
            if largest > self.__length:
                break

            if self.__heap[node] < self.__heap[largest]:
                self.__swap(node, largest)
            node = largest

