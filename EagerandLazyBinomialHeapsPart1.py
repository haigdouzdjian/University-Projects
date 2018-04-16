import sys
sys.setrecursionlimit(1000000) # For resetting recursion limit

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.par = None

class Part1():
    def __init__(self): # In the book
        self.root = None

    # Insert
    def insert(self, z): # In the book
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.par = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    # Maximum
    def maximum(self, x): # In the book
        while x.right != None:
            x = x.right
        return x

    # Minimum
    def minimum(self, x): # In the book
        while x.left != None:
            x = x.left
        return x

    # Remove
    def transplant(self, u, v): # In the book... for remove
        if u.par == None:
            self.root = v
        elif u == u.par.left:
            u.par.left = v # This is where I copied the book straight up
        else:
            u.par.right = v
        if v != None:
            v.par = u.par

    def remove(self, z): # In the book
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.par != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.par = y
            self.transplant(z, y)
            y.left = z.left
            y.left.par = y

    # Search
    def search(self,x,k): # In the book
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    # Best Path Value
    def bpv(self, OGNode): # Andy helped a lot during lab and office hours for this
        if OGNode != None:
            left = self.bpv(OGNode.left)
            right = self.bpv(OGNode.right)
            LRMax = max(left, right)
            keyString = str(OGNode.key)
            fiveCountKey = keyString.count(str(5))
            LRMax += fiveCountKey
            return LRMax
        else:
            return 0 # If it is just return or pass it gives errors. Lab suggested to make it 0... it worked...

def OGDriver():
    OGTree = Part1()
    with open(sys.argv[1]) as f:
        numOfLines = int(f.readline().strip())
        for x in range(numOfLines):
            OGInput = f.readline().strip()

            # Insert
            if "insert" in OGInput:
                K = int(OGInput.split()[1]) # K being the input value as stated in directions
                OGNode = Node(K)
                OGTree.insert(OGNode)

            # Remove
            if "remove" in OGInput:
                K = int(OGInput.split()[1]) # K being the input value as stated in directions
                if OGTree.search(OGTree.root, K) != None:
                    OGNode = OGTree.search(OGTree.root, K)
                    OGTree.remove(OGNode)
                else:
                    print("TreeError") # As discription states

            # Search
            if "search" in OGInput:
                K = int(OGInput.split()[1]) # K being the input value as stated in directions
                if OGTree.search(OGTree.root, K) != None:
                    print("Found") # As discription states
                else:
                    print("NotFound") # As discription states

            # Best Path Value
            if OGInput == "bpv":
                if OGTree.root != None:
                    print(OGTree.bpv(OGTree.root))
                else:
                    print("TreeError")

if __name__ == "__main__":
    OGDriver()
