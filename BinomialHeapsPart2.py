'''
  Project 1
  Problem2.py
  Queue w/ Linked List (Single)

  CIS 313
  Haig Douzdjian

  Sources: 1) The professor and GTF were extremely helpful in office hours with explaining the print function and driver functionality
           2) The slides and piazza were very helpful and acted as my main source of information
           3) https://stackoverflow.com/questions/10880813/typeerror-sequence-item-0-expected-string-int-found (for print function errors)
           4) https://stackoverflow.com/questions/2456148/python-print-end (running into error where my list would have an extra space at the end causing a difference)
           5) Most of my code follows Page 11 and 19 of the professor's week 2, Linear Data Structures, slides.
           6) Of course more googling of syntax (Node information, Getter and Setter functions, exceptions, and driver functionality help)
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
        def getNext(self):
            return self.next
        def getOgData(self):
            return self.ogData
        def setNext(self, next):
            self.next = next

    def __init__(self):     # Straight forward
        self.head = None
        self.back = None

    def enqueue(self, x):       # GTF Helped A LOT HERE, had a lot of trouble connecting the dots but he walked me through it
        nNode = self.LLNode(x)
        if self.is_empty() is False:
            self.back.setNext(nNode)        # Uses the setter function for back number
            self.back = self.back.getNext()     # Uses the getter function to re-declare back number
            return self.back
        else:
            self.head = nNode       # GTF Helped
            self.back = nNode
            return None


    def dequeue(self):
        if self.is_empty() is False:        # GTF Helped A LOT HERE, had a lot of trouble connecting the dots but he walked me through it
            currentH = self.head        # We have to take this approach other just stating self.head.get..... will not work (GTF helped)
            self.head = currentH.getNext()      # Uses the getter function to re-declare head number
            return currentH.getOgData()
        else:
            return None

    def is_empty(self):     # Very similar to my problem1.py is_empty function
        if self.head is None:       # GTF Helped
            return True;
        else:
            return False;

def print_queue(s):         # Very similar to my problem1.py print function
    if s.is_empty() is True:
        print("Empty")
    else:
        emptyList = []          # The professor taught this approach in office hours
        ogCopy = copy.deepcopy(s)
        while ogCopy.is_empty() is False:
            emptyList.append(ogCopy.dequeue())
            #print(ogCopy.dequeue(), end = ' ')   # Worked but had an ending space that messed up the diff
        emptyList = ' '.join(map(str, emptyList))       # The professor taught this approach in office hours but I also had to google for help due to TypeError (Citation 3 at top)
        print(emptyList)

def driver():       # Very similar to my problem1.py driver
    s = SingleLL()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                s.enqueue(value)        # GTF Helped
            elif action == "dequeue":
                check = s.dequeue()     # GTF Helped
                if check is None:       # GTF Helped and a google search of proper excpetions
                    print("QueueError")
                else:
                    print(check)        # GTF Helped
            elif action == "print":
                print_queue(s)

if __name__ == "__main__":
    driver()
