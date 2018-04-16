#include <stdio.h>

int mask(int n) {
    unsigned long long wrapper = 0xFFFFFFFF;
    return ~(wrapper << n);

    // Created an unsigned long long variable as mentioned on piazza and then returned the (negated? ~) of that wrapper as it left shifts n...
}

int main(int argc, const char * argv[]) {
    printf("1 to 0x%X\n", mask(1));
    printf("2 to 0x%X\n", mask(2));
    printf("3 to 0x%X\n", mask(3));
    printf("5 to 0x%X\n", mask(5));
    printf("8 to 0x%X\n", mask(8));
    printf("16 to 0x%X\n", mask(16));
    printf("32 to 0x%X\n", mask(32));
    return 0;
}
