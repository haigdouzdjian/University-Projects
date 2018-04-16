import sys
sys.setrecursionlimit(1000000) # For resetting recursion limit

class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.par = None

class Part3():
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

    # To_List_PreOrder
    def to_list_preorder(self, x, OGList):
        if x != None:
            OGList.append(x.key)
            self.to_list_preorder(x.left, OGList)
            self.to_list_preorder(x.right, OGList)

    # To_List_Inorder
    def to_list_inorder(self, x, OGList):
        if x != None:
            self.to_list_inorder(x.left, OGList)
            OGList.append(x.key)
            self.to_list_inorder(x.right, OGList)

    # To_List_PostOrder
    def to_list_postorder(self, x, OGList):
        if x != None:
            self.to_list_postorder(x.left, OGList)
            self.to_list_postorder(x.right, OGList)
            OGList.append(x.key)

def OGDriver():
    OGTree = Part3()
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


            # Max
            if OGInput == "max":
                if OGTree.root != None: # If nothing is in the searchTree
                    print(OGTree.maximum(OGTree.root).key)
                else:
                    print("Empty") # As discription states

            # Min
            if OGInput == "min":
                if OGTree.root != None: # If nothing is in the searchTree
                    print(OGTree.minimum(OGTree.root).key)
                else:
                    print("Empty") # As discription states

            # PrePrint
            if OGInput == "preprint":
                if OGTree.root != None:
                    OGList = []
                    OGTree.to_list_preorder(OGTree.root, OGList)
                    stringList = ' '.join(str(x) for x in OGList)
                    print(stringList)
                else:
                    print("Empty") # As discription states

            # InPrint
            if OGInput == "inprint":
                if OGTree.root != None:
                    OGList = []
                    OGTree.to_list_inorder(OGTree.root, OGList)
                    stringList = ' '.join(str(x) for x in OGList)
                    print(stringList)
                else:
                    print("Empty") # As discription states

            # PostPrint
            if OGInput == "postprint":
                if OGTree.root != None:
                    OGList = []
                    OGTree.to_list_postorder(OGTree.root, OGList)
                    stringList = ' '.join(str(x) for x in OGList)
                    print(stringList)
                else:
                    print("Empty") # As discription states

if __name__ == "__main__":
    OGDriver()
