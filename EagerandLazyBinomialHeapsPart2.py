import sys

class Node():

    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None

class Part2():

    def init_helper(self, i: int, l: 'list of strings') -> Node:
        if i >= len(l):
            return None

        node = Node(l[i])
        node.left = self.init_helper(2 * i + 1, l) # As mentioned in Piazza
        node.right = self.init_helper(2 * i + 2, l) # As mentioned in Piazza
        return node

    def __init__(self, l: 'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(0, l) # As mentioned in Piazza

    # Customized To_List_Inorder
    def to_list_inorder(self, x, inputList, outputList):
        if x != None: # Andy suggested to customize to_list_inorder to get the proper parentheses.
            if x.left == None:
                pass
            else:
                outputList.append('(')
                self.to_list_inorder(x.left, inputList, outputList)
            outputList.append(x.key) # appends proper value
            if x.right == None:
                pass
            else:
                self.to_list_inorder(x.right, inputList, outputList)
                outputList.append(')')

    def parenthesizeTree(self, OGList):
        result = ''
        stringList = result.join(x for x in OGList)
        return stringList

    # Customized To_List_PostOrder
    def to_list_postorder(self, x, outputList): # I didn't see a reason to create another function when this is the only use for to_list_postorder
        if x != None:
            if x.left != None and x.right != None:
                OGDict = { # Used a dictionary because I thought it would be the easiest to pull from. Could have just made these variables but I like dicts better
                '*': self.to_list_postorder(x.left, outputList) * self.to_list_postorder(x.right, outputList),
                '+': self.to_list_postorder(x.left, outputList) + self.to_list_postorder(x.right, outputList),
                '-': self.to_list_postorder(x.left, outputList) - self.to_list_postorder(x.right, outputList)
                }
                if x.key == '*':
                    return OGDict['*']
                if x.key == '+':
                    return OGDict['+']
                if x.key == '-':
                    return OGDict['-']
            else:
                return int(x.key) # Office hours helped me with this... Definition does not work without it

def OGDriver():
    with open(sys.argv[1]) as f:
        numOfLines = int(f.readline().strip())
        OGInput = f.readline().strip().split()
        OGTree = Part2(OGInput)
        OGList = []
        OGTree.to_list_inorder(OGTree.root, OGInput, OGList)
        print(OGTree.parenthesizeTree(OGList))
        print(OGTree.to_list_postorder(OGTree.root, OGList))

    # OGList2 = []
    # test = ['+', '*', '3', '4', '2']
    # OGTree = Part2(test)
    # OGTree.to_list_inorder(OGTree.root, test, OGList2)
    # print("\n" + OGTree.parenthesizeTree(OGList2))
    # print(OGTree.to_list_postorder(OGTree.root, OGList2))

if __name__ == "__main__":
    OGDriver()
