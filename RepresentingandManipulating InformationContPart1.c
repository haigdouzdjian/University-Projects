#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

struct IntArray {
    int length;
    int *dataPtr;
};

struct IntArray* mallocIntArray(int length) {
    struct IntArray *returnValue = NULL;		// local variable to hold return value;
    returnValue = (struct IntArray *)malloc(sizeof(struct IntArray));  // allocate 1 struct on the heap.
    returnValue-> length = length;					// initilize size value.
    returnValue-> dataPtr = (int *) malloc (sizeof(int) * length);	// allocate N*integers on the heap.
    for(int i=0; i < returnValue->length; i++)
    {
        returnValue->dataPtr[i] = 0;				// initilize all memory to 0's.
    }
    return returnValue;				// return the pointer to the struct on the heap.
}

void freeIntArray(struct IntArray **arrayPtr) {
    if((arrayPtr != NULL) && ((*arrayPtr) != NULL) )
    {
        for(int i=0; i< (*arrayPtr)-> length; i++)			// un-init all memory to 0's.
        {
            (*arrayPtr)-> dataPtr[i] = 0;
        }
        free((*arrayPtr)->dataPtr);			// de-allocate the array of integers.
        (*arrayPtr)->dataPtr =0;			// set the pointer to null.
        (*arrayPtr)->length =0;			// set the size to 0.
        free((*arrayPtr));				// free the struct pointer.
        (*arrayPtr) = 0;				// set value of the passed in pointer to null.
    }
    else
    {
        fprintf(stderr,"Error in BinArray_Free, bad pointer found.\n");
        exit(1);
    }
}

unsigned int ParseInt(char *buffer,int length)
{
    int position =0;			// variable to keep track of current index.
    int negative=+1;				// flag for signed values.
    int z = 0;

    if(buffer == NULL)
    {
        exit(1);
    }
    if(buffer[position] == '-')		// check for optional signed value, do not inc
    {
        negative =-1;			// set the flag and increment the index.
        position++;
    }else if(buffer[position] == '+')
    {
    }

    for (; position < length; position++) {
        char chara = buffer[position];
        switch(chara){
            case '0': z = z *10; z = z + 0; break;
            case '1': z = z *10; z = z + 1; break;
            case '2': z = z *10; z = z + 2; break;
            case '3': z = z *10; z = z + 3; break;
            case '4': z = z *10; z = z + 4; break;
            case '5': z = z *10; z = z + 5; break;
            case '6': z = z *10; z = z + 6; break;
            case '7': z = z *10; z = z + 7; break;
            case '8': z = z *10; z = z + 8; break;
            case '9': z = z *10; z = z + 9; break;
            case '\n' : break;
            case '\r' : break;
            case 0 : break;
            default: // We do this to acount for the cases not defined above (2^8 = 256 overall cases I believe is was Roscoe said)
                exit(1); //Exits
                break;
        }
    }
    z = z * negative;
    return z;
}

int readArray(FILE *ptr) {
    char buffer[BUFFER_SIZE];			// local array to store characters.
    int i = 0;
    for( i=0; i < BUFFER_SIZE;i++)		// zeri the array.
    {
        buffer[i] =0;
    }
    char c = 0;
    i = 0;
    do
    {
        c=getc(ptr);
        buffer[i++] = c;
    }
    while( (c != EOF) && (c != '\n'));

    return ParseInt(buffer, strlen(buffer));
}

void readIntArray(struct IntArray *array) { // Check this
    char buffer[BUFFER_SIZE];
    int a;
    int i = 0;
    for (i = 0; a < array->length; i++) {
        fprintf(stdout, "inter Int: ");
        a = readArray(stdin);
        array->dataPtr[i] = a;
    }
}

void swap(int *xp, int *yp) {  // Geek For Geek
    int placeHolder = *xp;
    *xp = *yp;
    *yp = placeHolder;
}

void sortIntArray(struct IntArray *array)
{
    int i, j;
    for (i = 0; i < array->length -1; i++)

        // Last i elements are already in place
        for (j = 0; j < array->length -i- 1; j++)
            if (array->dataPtr[j] > array->dataPtr[j+1]){
                swap(&(array->dataPtr[j]), &(array->dataPtr[j+1]));
            }
}


void printIntArray(struct IntArray *array) {
    for (int a = 0; a < array->length; a++){
        printf("%d", array->dataPtr[a]);
    }

}



int main(int argc, const char * argv[]) {
    int count;						// local variable to store count.
    fprintf(stdout,"Read Integer Number Value:");
    count = readArray(stdin);				// read a count .
    printf("%d\n", count);
    struct IntArray *test = mallocIntArray(count);		// allocate a BinArray of size count.
    readIntArray(test);
    sortIntArray(test);
    printIntArray(test);
    freeIntArray(&test);


    return EXIT_SUCCESS;
}
