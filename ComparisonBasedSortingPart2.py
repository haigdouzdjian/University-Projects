# https://www.tutorialspoint.com/python/list_index.htm
# https://stackoverflow.com/questions/13704860/zip-lists-in-python
# https://stackoverflow.com/questions/100732/why-is-if-not-someobj-better-than-if-someobj-none-in-python

import sys

def part2(): # Had lots of help with this
    with open(sys.argv[1]) as f:
        firstLine = f.readline().strip() # Reading first line
        for line in f: # Reading each line per iteration
            ogStack = []
            zipping = zip(list('<{[('), list('>}])')) # firsts and seconds
            ogDict = dict(zipping) # Cuz its OG :)
            for ch in line:
                if ch in list('<{[('):
                    ogStack.append(ogDict[ch])
                elif ch in list('>}])'):
                    if ch != ogStack.pop():
                        print("NO")
                        break
            if not ogStack: # Boolean Value Check (Cited ABove)
                print("YES")
    return

if __name__ == '__main__':
    part2()
