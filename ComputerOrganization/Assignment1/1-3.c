// Olivia Pannell
// Assignment 1- Question 3
#include <stdio.h>
int evenBit(unsigned int x)
{
  //make 0101 into a mask
  unsigned int mk;
  mk = 0x5;
  x = x & mk;
  return !!x;
}

int main()
{
  printf("evenBit(0x1) : %x\n", evenBit(0x1));
  printf("evenBit(0x2) : %x\n", evenBit(0x2));
  printf("evenBit(0x3) : %x\n", evenBit(0x3));
  printf("evenBit(0x4) : %x\n", evenBit(0x4));
  printf("evenBit(0xFFFFFFFF) : %x\n", evenBit(0xFFFFFFFF));
  printf("evenBit(0xAAAAAAAA) : %x\n", evenBit(0xAAAAAAAA));
  printf("evenBit(0x55555555) : %x\n", evenBit(0x55555555));

  return 0;
}
