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
        self.bhsize -= 1
        self.sift_down(1)
        return minimum

    def look(self) -> "comparable":
        if self.bhsize == 0:
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
class maximumHeap:
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
        if left <= self.bhsize and  self.array[left] > self.array[smallest]:
            smallest = left
        if right <= self.bhsize and self.array[right] > self.array[smallest]:
            smallest = right
        if smallest != i:
            x = self.array[i]
            self.array[i] = self.array[smallest]
            self.array[smallest] = x
            self.sift_down(smallest)

    def sift_up(self, i: int) -> None:
        parent = i // 2
        while i > 1 and self.array[parent] < self.array[i]:
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
        self.bhsize -= 1
        self.sift_down(1)
        return minimum

    def look(self) -> "comparable":
        if self.bhsize == 0:
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

# max heap on the left (smaller)
# Between first 2 (after very first line) smaller one on left and larger on right
#while loop to compare between look methods of each (for remaining numbers) and see which one it should go into

#if len of min heap = len max heap +2, then insert into max heap the removed element from the min heap.
def part2():

    # Declaring Heaps and List:
    minHeap = mininumHeap()
    maxHeap = maximumHeap()
    OGList = []

    # File Access
    with open(sys.argv[1]) as f:
        numOfLines = int(f.readline())
        for x in range(numOfLines):
            line = int(f.readline().strip())
            OGList.append(line)

        def mean(one, two):
            print((one + two) / 2)

        element = 0;


        # Base Cases: # Andy helped me set up base cases in office hours (drew a picture)
        if len(OGList) == 1: # If only one element, we print it
            print(int(OGList[0]))
        else:
            if OGList[0] >= OGList[1]: # Larger number goes in minHeap, smaller number in maxHeap. Put them in either one if they are equal
                minHeap.insert(OGList[0])
                maxHeap.insert(OGlist[1])
                print(OGList[0])
                mean(OGList[0], OGList[1])
                OGList = OGList[2:] # We do this so we can iterate through the rest of the list without the base cases
            else: # Large number goes in minHeap, smaller number in maxHeap
                minHeap.insert(OGList[1])
                maxHeap.insert(OGList[0])
                print(OGList[0])
                mean(OGList[0], OGList[1])
                OGList = OGList[2:] # We do this so we can iterate through the rest of the list without the base cases

            # Rest of List:
            while element < len(OGList): # I use a while loop because a for loop kept giving me an index error and Andy said to use this instead.
                # minHeap Insert from List
                if OGList[element] == minHeap.look() or OGList[element] > minHeap.look():
                    minHeap.insert(OGList[element])
                # maxHeap Insert from List
                elif OGList[element] == maxHeap.look() or OGList[element] < minHeap.look() or OGList[element] > maxHeap.look():
                    maxHeap.insert(OGList[element])

                # Re-Balancing maxHeap and Print
                if len(minHeap) > len(maxHeap) + 1: # Andy helped me set this up in office hours
                    maxHeap.insert(minHeap.remove())

                # Re-Balancing minHeap
                elif len(maxHeap) > len(minHeap) + 1: # Andy helped me set this up in office hours
                    minHeap.insert(maxHeap.remove())

                # Print minHeap.look() Case
                if len(minHeap) > len(maxHeap):
                    print(minHeap.look())

                # Print maxHeap.look() Case
                if len(maxHeap) > len(minHeap):
                    print(maxHeap.look())

                # Print Median Case (Mean)
                if len(minHeap) == len(maxHeap):
                    mean(minHeap.look(), maxHeap.look())

                # Continue Iteration Plus One
                element += 1;



if __name__ == "__main__":
    part2()
