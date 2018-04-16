#include <stdio.h>

int decode(int x, int y, int z) {
    // y to ey
    int ey = y;
    // makes ey equal to itself minus z
    ey = ey - z;
    // creates new ey to eyShift
    int eyShift = ey;
    // shifts eyShift to the left
    eyShift = eyShift << 31;
    // shifts eyShift to the right
    eyShift = eyShift >> 31;
    // make ey equal to itself times x
    ey = ey * x;
    // makes eyShift equal to itself (exclusive or) with ey
    eyShift = eyShift ^ ey;

    return eyShift;
}

// movl 12(%ebp), %edx
// subl 16(%ebp), %edx
// movl %edx, %eax
// imull 8(%ebp), %edx
// sall $31, %eax
// sarl $31, %eax
// xorl %edx, %eax

int main(int argc, const char * argv[]) {
    printf("Answer: %d\n", decode(1, 2, 4));
    printf("Answer: %d\n", decode(-4, -8, -12));

    return 0;
}
