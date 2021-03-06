import sys
sys.setrecursionlimit(1000000) # For resetting recursion limit

class Node():
    def __init__(self, key, color, value, val):
        self.left = value
        self.right = value
        self.key = key
        self.par = value
        self.color = color
        self.val = val

OGSentinel = Node(None, 'Black', None, None)

class Part1:
    def __init__(self): # In the book
        self.root = OGSentinel

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

class OGMap: # ANDY WENT OVER THIS ON THE BOARD IN OFFICE HOURS ON THURSDAY
    def __init__(self):
        self.OGTree = Part1()

    def newSearch(self, K):
        if self.OGTree.search(self.OGTree.root, K) == OGSentinel:
            raise exception
        return self.OGTree.search(self.OGTree.root, K).val

    def insert(self, K, V):
        self.OGTree.insert(Node(K, "Red", OGSentinel, V))

    def reassign(self, K, V):
        if self.OGTree.search(self.OGTree.root, K) != OGSentinel:
            self.OGTree.search(self.OGTree.root, K).val = V
        else:
            raise exception

    def remove(self, K):
        if self.OGTree.search(self.OGTree.root, K) != OGSentinel:
            self.OGTree.remove(self.OGTree.search(self.OGTree.root, K))
        else:
            raise exception

    def lookup(self, K):
        if self.OGTree.search(self.OGTree.root, K) != OGSentinel:
            return True
        else:
            return False



def OGDriver(): # ANDY WENT OVER THIS ON THE BOARD IN OFFICE HOURS ON THURSDAY
    OGMapInputOne = OGMap()
    OGMapInputTwo = OGMap()
    with open(sys.argv[1]) as f:
        numOfLinesOne, numOfLinesTwo = f.readline().strip().split()
        lineInputOne = f.readline().strip().split()
        lineInputTwo = f.readline().strip().split()
        complete = False;
        condition = 0

        def reassignHelper(z, pos):
            y = z.newSearch(pos)
            y += 1
            return y

        while(complete is False):
            # Map One
            for a in lineInputOne:
                if OGMapInputOne.lookup(a) != True:
                    OGMapInputOne.insert(a, 1)
                else:
                    OGMapInputOne.reassign(a, reassignHelper(OGMapInputOne, a))

            # Map Two
            for b in lineInputTwo:
                if OGMapInputTwo.lookup(b) != True:
                    OGMapInputTwo.insert(b, 1)
                else:
                    OGMapInputTwo.reassign(b, reassignHelper(OGMapInputTwo, b))

            # Word Checker
            for x in lineInputOne:
                if x not in lineInputTwo:
                    condition = 1
                    complete = True
                else:
                    if OGMapInputOne.newSearch(x) < OGMapInputTwo.newSearch(x):
                        condition = 1
                        complete = True

            condition = 2
            complete = True

        if condition is 1:
            print("NO")
        elif condition is 2:
            print("YES")

if __name__ == "__main__":
    OGDriver()
