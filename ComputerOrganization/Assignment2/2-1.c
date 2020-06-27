//Olivia Pannell
//Assignment 2 Question 1
#include <stdio.h>
int mask(int n)
{
  unsigned int mk;
  int x  = 32 - n;
  mk = 0xFFFFFFFF;
  mk = mk << x;
  mk = mk >> x;

  return mk;

}
int main()
{
  printf("mask(1): %x\n", mask(1));
  printf("mask(2): %x\n", mask(2));
  printf("mask(3): %x\n", mask(3));
  printf("mask(5): %x\n", mask(5));
  printf("mask(8): %x\n", mask(8));
  printf("mask(16): %x\n", mask(16));
  printf("mask(31): %x\n", mask(31));

  return 0;
}
