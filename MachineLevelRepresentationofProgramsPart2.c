//  .L3:
//  movl (%edx), %esi   --  I believe this means esi = (edx) so the value of esi -> pointer at (edx). (esi = index registers)
//  movl (%eax), %ecx   --  I believe this means ecx = (eax) so the value of ecx -> pointer at (eax). (ecx = general purpose/interchangable)
//  addl $4, %eax       --  Adds 4 to the value at %eax. (eax = general purpose/interchangable)
//  addl $40, %edx      --  Adds 40 to the value at %edx. (edx = general purpose/interchangable)
//  movl %esi, -4(%eax) --  Same thing as saying 'movl %esi, (%eax)' and moving this above the adl's above... From there I believe the pointer at eax = the value at esi... (eax) = esi
//  movl %ecx, -40(%edx)--  Same thing as saying 'movl %ecx, (%edx)' and moving this above the adl's above... From there I believe the pointer at edx = the value at ecx... (edx) = exc
//  cmpl %ebx, %eax     --  Compares values at %ebx to value at %eax
//  jne .L3             -- Jump to the loop if false

#include <stdio.h>

#define N 4
typedef int array_t[N][N];

void transpose(array_t a) {
    int *rp;
    int *cp;
    for (int i = 0; i < N; ++i) {
        rp = &a[i][0];
        cp = &a[0][i];
        for (int j = 0; j < i; ++j) {
            int tx = *rp; // Manually did a swap instead of just calling it
            int ty = *cp;
            *rp = ty;
            *cp = tx;
            rp = rp + 1;
            cp = cp + N; // N * 1 which just is equal to N
        }
    }
}

void printFunc(array_t a) {
    for (int x = 0; x < N; x++){
        for (int y = 0; y < N; y++){
            printf("%d ", a[x][y]); // Was not sure if this should be in nested arrays or not so I just printed the sequence instead
        }
    }

}


int main(int argc, const char * argv[]) {
    array_t ogArray = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    transpose(ogArray);
    printFunc(ogArray);
    return 0;
}
