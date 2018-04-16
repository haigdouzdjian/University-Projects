#define N 4
typedef int array_t[N][N];

void f(array_t a, int x, int y) { // int type can have negative and positive... unsigned int is only positive... So keep int because seg fault and regular errors shouldn't happen
    int xy = x * y; // We do here so we do not do it during every iteration in the nested for loop
    for (int i = 0; i < N; ++i) {
        int z = i * xy;
        for (int j = 0; j < N; ++j) {
            a[i][j] = z + j;
            printf("%d ", a[i][j]);
        }
    }
}

int main(int argc, const char * argv[]) {
    array_t test = {{1,2,3,4}, {1,2,3,4}, {1,2,3,4}, {1,2,3,4}};
    f(test, 2,3);
    return 0;
}
