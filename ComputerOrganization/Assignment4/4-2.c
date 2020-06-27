//Olivia Pannell
//Assignment 4 Question 2
#include <stdio.h>

// int sum(int n) {
//  int i = 1;
//  int result = 0;
//  do {
//  result += i;
//  ++i;
//  } while (i <= n);
//  return result;
// }

long sum(long n)
{
  if (n < 1)
  {
    return 0;
  }
  long i = 1;
  long result = 0;
  // Ensure that argument *n* is in %rdi, *i* is in %rcx,
  // *result* is in %rax - do not modify.
  __asm__ ("movq %0, %%rdi # n in rdi;" :: "r" ( n ));
  __asm__ ("movq %0, %%rcx # i in rcx;" :: "r" ( i ));
  __asm__ ("movq %0, %%rax # result in rax;" :: "r" ( result ));

  // Your x86-64 code goes in the __asm__ block below -
  // comment each instruction...

  __asm__(
    ".loop:" // #beginning of loop
    "addq %rcx, %rax;" // # Adds result and i together and puts it in result
    "addq $1, %rcx;" // # Adds 1 to the counter
    "cmpq %rcx, %rdi;" // #Compares i and n
    "jle .loop;" // # jumps if i is less than or equal to n
    );

  // Ensure that *result* is in %rax for return - do not modify.
  __asm__ ("movq %%rax, %0 #result in rax;" : "=r" ( result ));

  return result;
}
int main()
{
  printf("sum(1): %ld\n", sum(1));
  printf("sum(3): %ld\n", sum(3));
  printf("sum(5): %ld\n", sum(5));
  printf("sum(7): %ld\n", sum(7));

  return 0;
}
