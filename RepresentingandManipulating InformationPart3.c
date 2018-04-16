#include <stdio.h>

int ge(float x, float y) {
    unsigned ux = *((unsigned *) &x); // convert x raw bits
    unsigned uy = *((unsigned *) &y); // convert y raw bits
    unsigned sx = ux >> 31; // extract sign bit of ux
    unsigned sy = uy >> 31; // extract sign bit of uy
    ux <<= 1; // drop sign bit of ux
    uy <<= 1; // drop sign bit of uy

    int a = (uy == 0) && (ux == 0);
    int b = (uy <= ux) && (sy >= sx);
    int c = sx < sy;

    return a || b || c;
    
    // Both 0 (both positive, both negative, and other), x is neg and y is post, switched, both positive, both are neg
}

int main(int argc, const char * argv[]) {
    printf("0.0f , 0.0f to 0x%X\n", ge(0.0f, 0.0f));
    printf("-0.0f , 0.0f to 0x%X\n", ge(-0.0f, 0.0f));
    printf("-1.0f , 0.0f to 0x%X\n", ge(-1.0f, 0.0f));
    printf("0.0f , 1.0f to 0x%X\n", ge(0.0f, 1.0f));
    printf("1.0f , 0.0f to 0x%X\n", ge(1.0f, 0.0f));
    printf("0.0f , -1.0f to 0x%X\n", ge(0.0f, -1.0f));
    return 0;
}
