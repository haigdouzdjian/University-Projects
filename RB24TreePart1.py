import sys
sys.setrecursionlimit(1000000) # For resetting recursion limit

class Node():
    def __init__(self, key, color, value):
        self.OGSize = 0 # Andy's idea in office hours
        self.left = value
        self.right = value
        self.key = key
        self.par = value
        self.color = color

class Part1():
    def __init__(self): # In the book and STUDENTS/ANDY IN OFFICE HOURS WERE VERY HELPFUL.... One of the students gave me his idea of doing kthstatistic and tree size and the insert counter, brilliant!!!!!!!!!!
        self.kthStatistic = 0 # Andy's idea in office hours
        self.root = OGSentinel
        self.OGTreeSize = 0 # Andy's idea in office hours

    # Left_Rotate
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != OGSentinel:
            y.left.par = x
        y.par = x.par
        if x.par == OGSentinel:
            self.root = y
        elif x == x.par.left:
            x.par.left = y
        else:
            x.par.right = y
        y.left = x
        x.par = y

    # Right_Rotate
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != OGSentinel:
            y.right.par = x
        y.par = x.par
        if x.par == OGSentinel:
            self.root = y
        elif x == x.par.left:
            x.par.left = y
        else:
            x.par.right = y
        y.right = x
        x.par = y

    # Insert_Fixup
    def insert_fixup(self, z):
        while z.par.color == 'Red':
            if z.par == z.par.par.left:
                y = z.par.par.right
                if y.color == 'Red':
                    z.par.color = 'Black'
                    y.color = 'Black'
                    z.par.par.color = 'Red'
                    z = z.par.par
                elif z == z.par.right:
                    z = z.par
                    self.left_rotate(z)
                else:
                    z.par.color = 'Black'
                    z.par.par.color = 'Red'
                    self.right_rotate(z.par.par)
            else:
                y = z.par.par.left
                if y.color == 'Red':
                    z.par.color = 'Black'
                    y.color = 'Black'
                    z.par.par.color = 'Red'
                    z = z.par.par
                elif z == z.par.left:
                    z = z.par
                    self.right_rotate(z)
                else:
                    z.par.color = 'Black'
                    z.par.par.color = 'Red'
                    self.left_rotate(z.par.par)
        self.root.color = 'Black'

    # Insert
    def insert(self, z): # In the book
        y = OGSentinel
        x = self.root
        while x != OGSentinel:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.par = y
        if y == OGSentinel:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = OGSentinel
        z.right = OGSentinel
        z.color = 'Red'
        self.insert_fixup(z)
        self.OGTreeSize += 1

    # Remove
    def transplant(self, u, v):
        if u.par == OGSentinel:
            self.root = v
        elif u == u.par.left:
            u.par.left = v
        else:
            u.par.right = v
        v.par = u.par

    # Maximum
    def maximum(self, x): # In the book
        while x.right != OGSentinel:
            x = x.right
        return x

    # Minimum
    def minimum(self, x): # In the book
        while x.left != OGSentinel:
            x = x.left
        return x

    def delete_fixup(self, x):
        while x != self.root and x.color == 'Black':
            if x == x.par.left:
                w = x.par.right
                if w.color == 'Red':
                    w.color = 'Black'
                    x.par.color = 'Red'
                    self.left_rotate(x.par)
                    w = x.par.right
                if w.left.color == 'Black' and w.right.color == 'Black':
                    w.color = 'Red'
                    x = x.par
                elif w.right.color == 'Black':
                    w.left.color = 'Black'
                    w.color = 'Red'
                    self.right_rotate(w)
                    w = x.par.right
                else:
                    w.color = x.par.color
                    x.par.color = 'Black'
                    w.right.color = 'Black'
                    self.left_rotate(x.par)
                    x = self.root
            else:
                w = x.par.left
                if w.color == 'Red':
                    w.color = 'Black'
                    x.par.color = 'Red'
                    self.right_rotate(x.par)
                    w = x.par.left
                if w.right.color == 'Black' and w.left.color == 'Black':
                    w.color = 'Red'
                    x = x.par
                elif w.left.color == 'Black':
                    w.right.color = 'Black'
                    w.color = 'Red'
                    self.left_rotate(w)
                    w = x.par.left
                else:
                    w.color = x.par.color
                    x.par.color = 'Black'
                    w.left.color = 'Black'
                    self.right_rotate(x.par)
                    x = self.root
        x.color = 'Black'

    def remove(self, z):
        y = z
        y_original_color = y.color
        if z.left == OGSentinel:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == OGSentinel:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.par == z:
                x.par = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.par = y
            self.transplant(z, y)
            y.left = z.left
            y.left.par = y
            y.color = z.color
        if y_original_color == 'Black':
            self.delete_fixup(x)

    # Search
    def search(self,x,k): # In the book
        if x == OGSentinel or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    # To_List_Inorder
    def to_list_inorder(self, x, OGList):
        if x != OGSentinel:
            self.to_list_inorder(x.left, OGList)
            OGList.append(x.key)
            self.to_list_inorder(x.right, OGList)

    def get_subtree_sizes(self, x): # Andy ran through it in office hours on the whiteboard
        if x != OGSentinel:
            left = self.get_subtree_sizes(x.left)
            right = self.get_subtree_sizes(x.right)
            newSize = left + right + 1
            x.OGSize = newSize
            return newSize
        else:
            return 0

    def memoryStat(self, x):
        self.kthStatistic = x.key

    def sizeChecker(self, z, sign):
        if sign == 'add':
            res = z.OGSize + 1
        if sign == 'none':
            res = z.OGSize
        return res

    def order_statistic(self, x, k): #  # Andy ran through it in office hours on the whiteboard --- VERY HELPFUL THANK YOU!
        if x != OGSentinel:
            if self.sizeChecker(x.left, 'add') == k:
                self.memoryStat(x)
                return
            if self.sizeChecker(x.left, 'add') > k:
                self.order_statistic(x.left, k)
            if self.sizeChecker(x.left, 'add') < k:
                self.order_statistic(x.right, (k - self.sizeChecker(x.left, 'none'))- 1)
            return self.kthStatistic

# https://stackoverflow.com/a/19188032
    # def OGTreeSize(OGRoot, counter = 0):
    # if OGRoot is None:
    #     return counter
    # return OGTreeSize(OGRoot.left, OGTreesize(OGRoot.right, counter + 1))


OGSentinel = Node(None, 'Black', None)


def OGDriver():
    OGTree = Part1()
    with open(sys.argv[1]) as f:
        numOfLines = int(f.readline().strip())
        for x in range(numOfLines):
            OGInput = f.readline().strip()

            # Insert
            if "insert" in OGInput:
                K = int(OGInput.split()[1]) # K being the input value as stated in directions
                OGNode = Node(K, 'Red' ,OGSentinel, )
                OGTree.insert(OGNode)

            # Remove
            if "remove" in OGInput:
                K = int(OGInput.split()[1]) # K being the input value as stated in directions
                if OGTree.search(OGTree.root, K) != OGSentinel:
                    OGNode = OGTree.search(OGTree.root, K)
                    OGTree.remove(OGNode)
                else:
                    print("TreeError") # As discription states

            # Search
            if "search" in OGInput:
                K = int(OGInput.split()[1]) # K being the input value as stated in directions
                if OGTree.search(OGTree.root, K) != OGSentinel:
                    print("Found") # As discription states
                else:
                    print("NotFound") # As discription states

            # Max
            if OGInput == "max":
                if OGTree.root != OGSentinel: # If nothing is in the searchTree
                    print(OGTree.maximum(OGTree.root).key)
                else:
                    print("Empty") # As discription states

            # Min
            if OGInput == "min":
                if OGTree.root != OGSentinel: # If nothing is in the searchTree
                    print(OGTree.minimum(OGTree.root).key)
                else:
                    print("Empty") # As discription states

            # InPrint
            if OGInput == "inprint":
                if OGTree.root != OGSentinel:
                    OGList = []
                    OGTree.to_list_inorder(OGTree.root, OGList)
                    stringList = ' '.join(str(x) for x in OGList)
                    print(stringList)
                else:
                    print("Empty") # As discription states

            if "get_subtree_sizes" in OGInput:
                OGTree.get_subtree_sizes(OGTree.root)

            if "order" in OGInput: # Andy helped in office hours
                K = int(OGInput.split()[1]) # K being the input value as stated in directions
                if 1 > K or OGTree.OGTreeSize < K:
                    print("TreeError")
                else:
                    print(OGTree.order_statistic(OGTree.root, K))

if __name__ == "__main__":
    OGDriver()
