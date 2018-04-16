#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Block {

    unsigned char value[4];
    unsigned int tag;
    unsigned char valid;
};

unsigned int getOffset(unsigned int addr){
    return (addr & 0x3);
}

unsigned int getSet(unsigned int addr){
    return (addr>>2) & 0xf;
}

unsigned int getTag(unsigned int addr){
    return (addr>>6);
}

int main(int argc, char* argv[]) {
    struct Block *cache = (struct Block*) malloc(16 * sizeof(struct Block));
    for (int i = 0; i < 16; i++){
        cache[i].valid = '0';
    }
    bool completed = false;
    unsigned int userAddress;
    unsigned int userValue;
    char inp[256];
    char c;

    while (!completed){
        printf("Enter 'r' for read, 'w' for write, 'p' to print, 'q' to quit: ");
        scanf("%s", inp);
        c = inp[0];

        // Write
        if (c == 'w') {
            printf("Enter 32-bit unsigned hex address: ");
            scanf("%x", &userAddress);
            printf("Enter 32-bit unsigned hex value: ");
            scanf("%x", &userValue);
            struct Block *newBlock = &cache[getSet(userAddress)];
            unsigned char *up = (unsigned char *)&userValue;

            if (newBlock->valid == '1') {
                printf("Evicting block - tag: %d - set: %c - valid: %c - value: %.2x %.2x %.2x %.2x \n", getTag(userAddress), getSet(userAddress), newBlock->valid, newBlock->value[0], newBlock->value[1], newBlock->value[2], newBlock->value[3]);
            }
            else {
                newBlock->valid = '1';
            }
            for (int i = 0; i < 4; ++i) {
                newBlock->value[i] = up[i];
            }
            printf("Wrote tag: %d - set: %d - valid: %c - value: %.2x %.2x %.2x %.2x \n", getTag(userAddress), getSet(userAddress), newBlock->valid, newBlock->value[0], newBlock->value[1], newBlock->value[2], newBlock->value[3]);
        }

        // Read
        else if (c == 'r') {
            printf("Enter 32-bit unsigned hex address: ");
            scanf("%x", &userAddress);
            printf("Looking for tag: %d - set: %d\n", getTag(userAddress), getSet(userAddress));
            struct Block *newBlock = &cache[getSet(userAddress)];
            if (newBlock->valid == '1') {
                printf("Found tag: %d - set: %d - offset: %d - valid: %d -value: %x\n", newBlock->tag, getSet(userAddress), getOffset(userAddress), newBlock->valid, newBlock->value[(getOffset(userAddress))]);
                if (newBlock->tag == getTag(userAddress)){
                    printf("Hit");
                }
                else {
                    printf("Miss, tags not the same");
                }
            }
            else {
                printf("Miss, valid set not found");
            }
        }

        // Print
        else if (c == 'p') { // Second line is messsssssssssssssed up
            for (int i = 0; i < 16; i++) {
                if(cache[i].valid == '1'){
                    printf("tag: %d - set: %d - valid: %d - value: %x %x %x %x\n", cache[i].tag, i, cache[i].valid, cache[i].value[0], cache[i].value[1], cache[i].value[2], cache[i].value[3]);
                    printf("\n");
                }
            }
        }

        // Quit
        else if (c == 'q') {
            completed = true;
        }
    }
}
