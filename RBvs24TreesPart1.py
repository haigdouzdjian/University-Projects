import sys

class mininumHeap:
    class Underflow(Exception):
        def __init__(self, data = None):
            super().__init__(data)
    def __init__(self, array = None):
        if array == None:
            self.bhsize= 0
            self.length= 1025
            self.array= [None] * self.length
        else:
            self.length= len(array) + 1
            self.array= [None] * self.length
            for i in range(len (array)):
                self.array[i+1] = array[i]
            self.bhsize= self.length- 1
            i = self.length// 2
            while i > 0:
                self.sift_down(i)
                i -= 1
    def sift_down(self, i: int) -> None:
        left = 2 * i
        right = left + 1
        smallest = i
        if left <= self.bhsize and  self.array[left] < self.array[smallest]:
            smallest = left
        if right <= self.bhsize and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != i:
            x = self.array[i]
            self.array[i] = self.array[smallest]
            self.array[smallest] = x
            self.sift_down(smallest)

    def sift_up(self, i: int) -> None:
        parent = i // 2
        while i > 1 and self.array[parent] > self.array[i]:
            x = self.array[parent]
            self.array[parent] = self.array[i]
            self.array[i] = x
            i = parent
            parent = i// 2

    def insert(self, x: "comparable") -> None:
        if self.bhsize >=  self.length - 1:     # self.length - 1 because we lower the threshold by 1
            nlength= 2 * self.length
            narray= [None] * nlength
            for i in range(1, self.bhsize+1):
                narray[i] = self.array[i]
            self.length= nlength
            self.array= narray
        self.bhsize += 1
        self.array[self.bhsize] = x
        self.sift_up(self.bhsize)

    def remove(self) -> "comparable":
        if self.bhsize== 0:
            raise BinaryHeap.Underflow("remove() called on empty heap")
        minimum = self.array[1]
        self.array[1] = self.array[self.bhsize]
        self.bhsize-= 1
        self.sift_down(1)
        return minimum

    def look(self) -> "comparable":
        if self.bhsize== 0:
            raise BinaryHeap.Underflow("look() called on empty heap")
        return self.array[1]

    def size(self) -> int:
        return self.bhsize

    def is_empty(self) -> bool:
        if self.bhsize== 0:
            return True
        else:
            return False

    def to_string(self) -> str:
        if self.bhsize== 0:
            result = 'Empty'
        else:
            l = []
            for i in range(1, self.bhsize+1):
                l.append(str  (self.array[i]))
            result = ' '.join(l)
        return result

    def __len__(self) -> int:
        return self.size()

    def __str__(self) -> bool:
        return self.to_string()

    def __iter__(self) -> "iterator":
        i = 1
        while i <= self.bhsize:
            yieldself.array[i]
            i += 1

def part1():
    OGHeap = mininumHeap()
    with open(sys.argv[1]) as f:
        numOfLines = f.readline()
        numOfLines = int(numOfLines.strip())
        for x in range(numOfLines):
            # Start A or B
            # Then estimated service time
            # Then iteration
            # Then IP
            preTuple = f.readline().strip().split()
            OGTuple = (preTuple[1], int(preTuple[2]), x, preTuple[0])
            # Tuple compares strings
            OGHeap.insert(OGTuple)
    for preTuple in range(OGHeap.size()):
        print(OGHeap.remove()[3]) # Prints removed address

if __name__ == "__main__":
    part1()
