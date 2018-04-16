#include <stdio.h>

//int sum(int from, int to) {
//    int result = 0;
//    do {
//        result += from;
//        ++from;
//    } while (from <= to);
//    return result;
//}

int sum(int from, int to) {
    int result = 0;
    __asm__ ("movl %0, %%ecx # from in ecx;" :: "r" ( from ));
    __asm__ ("movl %0, %%edx # to in edx;" :: "r" ( to ));
    __asm__ ("movl %0, %%eax # result in eax;" :: "r" ( result ));
    __asm__(".ogLoop:"); // Loop
            // "movl %edx, %eax # For example, this sets result = to;"
        __asm__("addl %ecx, %eax"); // result = result + from in code (result += from)
        __asm__("addl $1, %ecx"); // ++from in code
        __asm__("cmpl %edx, %ecx"); // compare to and from
        __asm__("jle .ogLoop"); // if from is <= to to, jump to top of loop again
    __asm__ ("movl %%eax, %0 #result in eax;" : "=r" ( result ));
    return result;
}

int main(int argc, const char * argv[]) {
    printf("%d\n", sum(1, 6));
    printf("%d\n", sum(3, 5));
    return 0;
}
