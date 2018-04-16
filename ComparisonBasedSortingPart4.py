# The book page 154 and office hours

import sys
class Min_Heap:
    def __init__(self):
        self.ogList = []
        self._size = 0

    def Right(self, i):
        return 2*i

    def Left(self, i):
        return 2*i+1

    def insert(self, x):
        self.ogList.append(x)
        self._size += 1
        # self.

    def remove(self):
        if self.size() == 0:
            return "HeapError"
        else:
            self.ogList.pop()

    def look(self):
        if self._size == 0:
            return "HeapError"
        else:
            return self.heaplist[1]

    def size(self):
        return self._size

    def is_empty(self):
        return self.size == 0

    def to_string(self):
        if self.size() ==0:
            return "Empty"
        string = ""
        #for i in range(self.size()) # Ran out of time

    # def max-heapify(A, i):
    #     l D LEFT.i /
    #     r D RIGHT.i /
    #     if l <= A.heap-size and A[l] > A[i]
    #         largest = l
    #     else largest = i
    #     if r <= A.heap-size and A[r] > A[largest]
    #         largest = r
    #     if largest != i:
    #         exchange A[i] with A[largest]
    #         MAX-HEAPIFY(A, largest)
