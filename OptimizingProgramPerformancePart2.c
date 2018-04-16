#include <stdio.h>
#include <time.h>

void inner(float *u, float *v, int length, float *dest) {
    int i;
    float sum = 0.0f;
    for (i = 0; i < length; ++i) {
        sum += u[i] * v[i];
    }
    *dest = sum;
    printf("%f\n", *dest);
}

void inner2(float *u, float *v, int length, float *dest) {
    int i;
    int limit = length - 3;
    float s0 = 0.0f;
    float s1 = 0.0f;
    float s2 = 0.0f;
    float s3 = 0.0f;
    for (i = 0; i < limit; i+=4) {
        s0 += u[i] * v[i];
        s1 += u[i+1] * v[i+1];
        s2 += u[i+2] * v[i+2];
        s3 += u[i+3] * v[i+3];
    }
    for (; i < length; i++) {
        s0 += u[i] * v[i];
    }
    *dest = s0 + s1 + s2 + s3;
    printf("%f\n", *dest);
}

int main(int argc, const char * argv[]) {
    float arraya[3] = {1.0f, 1.0f, 1.0f};
    float arrayb[3] = {4.0f, 5.0f, 9.0f};
    float destination = 0.0f;
    clock_t start = clock();
    inner2(arraya, arrayb, 4, &destination);
    clock_t end = clock();
    double total = ((double) (end - start))/CLOCKS_PER_SEC;
    printf("%lu %lu %lf\n\n", start, end, total);

    clock_t start2 = clock();
    inner(arraya, arrayb, 4, &destination);
    clock_t end2 = clock();
    double total2 = ((double) (end2 - start2))/CLOCKS_PER_SEC;
    printf("%lu %lu %lf\n\n", start2, end2, total2);

}
