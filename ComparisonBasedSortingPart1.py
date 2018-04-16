
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
# https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary
# http://www.tutorialspoint.com/python/dictionary_get.htm


import sys

def part1():
    magHash = {}
    noteHash = {}

    with open(sys.argv[1]) as f:
        read = f.readline().strip().split(' ')
        numMags = int(read[0])  # Used to check if input is correct
        numNotes = int(read[1]) # Used to check if input is correct
        mag = f.readline().strip().split(' ')
        if len(mag) != numMags: # For real world application
            raise ValueError('Mag length is off!')
        note = f.readline().strip().split(' ')
        if len(note) != numNotes: # For real world application
            raise ValueError('Note length is off!')
        for z in mag:
            magHash[z] = magHash.get(z, 0) + 1 #GTF suggested I add +1 to each so it can go through properly
        for y in note:
            noteHash[y] = noteHash.get(y, 0) + 1 #GTF suggested I add +1 to each so it can go through properly
        for x in noteHash: # Note first because it is what are comparing to
            if x in magHash:
                if noteHash[x] > magHash[x]:# GTF gave suggestions for this
                    print("NO")
                    return # So it ends
            else:
                print("NO")
                return # So it ends
        print("YES")
        return # So it ends


if __name__ == "__main__":
    part1()
