from MaxHeap import MaxHeap

class pQueue(object):
    def __init__(self,size) :
        # Build the Constructor
        self.__myHeap = MaxHeap(size)

    def insert(self, data):
        self.__myHeap.insert(data)

    def maximum(self):
        return self.__myHeap.maximum()

    def extractMax(self):
        return self.__myHeap.extractMax()

    def isEmpty(self):
        return self.__myHeap.getLength() == 0

    def printQueue(self):
        s = "Current Queue: "
        heap = self.__myHeap.getHeap()
        for i in range(1, self.__myHeap.getLength()):
            s += str(heap[i])
            s += ','

        s += str(heap[self.__myHeap.getLength()])
        print(s)
