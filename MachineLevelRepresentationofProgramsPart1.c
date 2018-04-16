#include <stdio.h>

//loop:
//  pushl %ebp      --  Pushes base pointer onto the stack (ebp = used to access data on the stack)
//  movl %esp, %ebp --  Copies stack pointer to the base pointer (registers. Source Cited Above)
//  pushl %esi      --  Pushes esi onto the stack
//  pushl %ebx      --  Pushes ebx onto the stack
//  movl 8(%ebp), %esi  -- Gets x (8th location) and stored in esi
//  movl 12(%ebp), %ecx --  Gets y (12th location) and stored in ecx
//  movl $2, %edx   --  Changes the value of edx by 2
//  movl $-1, %eax  --  Changes the value of eax by 1
//.L2:
//  movl %esi, %ebx --  Moves esi to ebx
//  andl %edx, %ebx --  The mask (edx) & ebx
//  xorl %ebx, %eax --  Exclusive Or between ebx and eax
//  sall %cl, %edx  --  Shift edx by %cl
//  cmpl $1, %edx   --  If edx == 1
//  jg .L2          --  If above is true, jumps to the top of th loop
//  popl %ebx       --  Takes ebx off the stack
//  popl %esi       --  Takes esi off the stack
//  popl %ebp       --  Takes ebp off the stack
//  ret             --  Return


int loop(int x, int y) {
    int result = -1 ;
    for (int mask = 2 ; mask > 1 ; mask <<= y ) {
        result ^= (mask & x);
    }
    return result;
}

int main(int argc, const char * argv[]) {
    printf("%d\n", loop(1,5));
    printf("%d\n", loop(2,4));
    printf("%d\n", loop(3,3));
    printf("%d\n", loop(4,2));
    printf("%d\n", loop(5,1));
    return 0;
}
