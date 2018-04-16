#include <stdio.h>



unsigned int extract (unsigned int x, int i) {
    int location = (3 - i) << 3; // Producing position for i... using the help of left shift
    int wrapper = x << location; // Implementing i into the hex using left shift
    wrapper >>= 24; // Pulling the information needed back to the right side with the help of right shifting 24 (so it can back to the proper spot)
    return wrapper;

    // Returns byte i of x sign extended to 32 bits
}



int main(int argc, const char * argv[]) {
    printf("0x12345678 , 0 to 0x%X\n", extract(0x12345678, 0));
    printf("0xABCDEF00 , 2 to 0x%X\n", extract(0xABCDEF00, 2));
    return 0;
}
