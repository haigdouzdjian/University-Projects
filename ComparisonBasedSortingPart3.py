# https://docs.python.org/3/library/collections.html#collections.deque
# https://wiki.python.org/moin/TupleSyntax

import sys
from collections import deque

def part3(): # Had lots of questions that GTF answered
    beginPosition = 0
    availableEnergy = 0
    continueOn = True
    with open(sys.argv[1]) as f:
        read = f.readline().strip()
        ogList = []
        for line in range(int(read)): # Iterates through each line and appends to the list
            energyAndConsumed = f.readline().strip().split(' ')
            ogList.append([line, (int(energyAndConsumed[0]), int(energyAndConsumed[1]))]) # ex: (0, (4,2)) ... cited tuples above

        while continueOn is True: # Similar to problem from 212 where change the boolean statement at the end
            ogList = deque(ogList) #cited above, found on stackOverflow
            selected = ogList.popleft() #first item ex: (0, (4,2))
            result = ogList[0][0] # Because of the setup, ex: (0, (4,2)), the first element is a sort of like my counter/selected item.. Asked a GTF and he suggested it wasn't the best approach but not the worst
            restaurantNumber = selected[0]  # ex: (0, (4,2)) this would be 0
            energyGained = selected[1][0] # ex: (0, (4,2)) energy gained = 4
            energySpent = selected[1][1] # ex: (0, (4,2)) energy spent = 2
            availableEnergy = energyGained + availableEnergy # adds what we gained to what we have
            ogList.append(selected) # appends this back to cycle so you can move restaurants
            availableEnergy = availableEnergy - energySpent # the tax for moving from old restaurant to new restaurant
            beginPosition = 1 + restaurantNumber # I am so close... but ran out of time
            elif beginPosition == result:
                continueOn = False # ends the while loop
        print(beginPosition)
        return

if __name__ == "__main__":
    part3()
