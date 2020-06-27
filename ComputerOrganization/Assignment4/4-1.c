//Olivia Pannell
//Assignment 4 Question 1
#include <stdio.h>

//
// loop:

// movq %rsi, %rcx

// mask = 1
// movl $1, %edx

// result = 0
// movl $0, %eax

// .L2:

// testing if mask = 0
// testq %rdx, %rdx

// je .L4

// mask into r8
// movq %rdx, %r8

// a | mask into r8
// orq %rdi, %r8

// a | mask OR result into result
// orq %r8, %rax

//shift by mask
// sarq %cl, %rdx

// jmp .L2

// .L4:
// ret

long loop(long a, long b) {
 long result = 0;
 for (long mask = 1; mask != 0; mask >>= b)
 {
   result |= (a | mask);
 }
 return result;
}
int main()
{
  printf("loop(1, 5): %ld\n", loop(1, 5));
  printf("loop(2, 4): %ld\n", loop(2, 4));
  printf("loop(3, 3): %ld\n", loop(3, 3));
  printf("loop(4, 2): %ld\n", loop(4, 2));
  printf("loop(5, 1): %ld\n", loop(5, 1));
  return 0;

}
