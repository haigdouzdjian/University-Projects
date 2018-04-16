'''
  Project 1
  Problem1.py
  Stack w/ Linked List (Single)

  CIS 313
  Haig Douzdjian

  Sources: 1) The professor and GTF were extremely helpful in office hours with explaining the print function and driver functionality
           2) The slides and piazza were very helpful and acted as my main source of information
           3) https://stackoverflow.com/questions/10880813/typeerror-sequence-item-0-expected-string-int-found (for print function errors)
           4) https://stackoverflow.com/questions/2456148/python-print-end (running into error where my list would have an extra space at the end causing a difference)
           5) Most of my code follows Page 8 and 19 of the professor's week 2, Linear Data Structures, slides.
           6) Of course more googling of syntax (Node information, exceptions, and driver functionality help)
'''

import sys
import copy


class Underflow(Exception):
    pass

class SingleLL(object):
    class LLNode(object):
        def __init__(self, ogData = None):
            self.ogData = ogData # OG Foundation
            self.next = None

    def __init__(self):
        self.size = 0   # Never used, just swapped over from class notes (Week 2 page 19)
        self.head = None

    def push(self, x):       # GTF Helped A LOT HERE, walked me through the slide notes (Week 2 Page 19) and helped me put this together
        nNode = self.LLNode(x)      # Straight forward push function
        nNode.next = self.head
        self.head = nNode
        return str(x)

    def pop(self):       # GTF Helped A LOT HERE, walked me through the slide notes (Week 2 Page 19) and helped me put this together
        if self.is_empty() is True:     # Runs only if is_empty() is False
            return None
        else:
            elementPop = self.head.ogData      # Declares elementPop as a "holder" for the head number
            self.head = self.head.next      # Grabs next
            return str(elementPop)

    def is_empty(self):     # Very similar to my problem2.py is_empty function
        if self.head is None:       # GTF Helped
            return True;
        else:
            return False;

def print_stack(s):         # Very similar to my problem2.py print function
    if s.is_empty() is True:
        print("Empty")
    else:
        emptyList = []          # The professor taught this approach in office hours
        ogCopy = copy.deepcopy(s)
        while ogCopy.is_empty() is False:
            emptyList.append(ogCopy.pop())
            #print(ogCopy.pop(), end = ' ')   # Worked but had an ending space that messed up the diff
        emptyList = ' '.join(emptyList)         # The professor taught this approach in office hours
        print(emptyList)

def driver():       # Very similar to my problem2.py driver
    s = SingleLL()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                s.push(value)       # GTF Helped
            elif action == "pop":
                check = s.pop()         # GTF Helped
                if check is None:       # GTF Helped and a google search of proper excpetions
                    print("StackError")
                else:
                    print(check)        # GTF Helped
            elif action == "print":
                print_stack(s)

if __name__ == "__main__":
    driver()
