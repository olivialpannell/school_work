// Olivia Pannell
// Assignment 1- Question 1
#include <stdio.h>
unsigned int combine(unsigned int x, unsigned int y)
{
  //get rid of the last 6 bits and replace them with zero
  x = x >> 24;
  x = x << 24;


  //get rid of first 2 bits nd replace them with zero
  y = y << 8;
  y = y >> 8;


  return x | y;
}
int main()
{
  printf("combine(0x12345678, 0xABCDEF00): %x\n", combine(0x12345678, 0xABCDEF00));
  printf("combine(0xABCDEF00, 0x12345678): %x\n", combine(0xABCDEF00, 0x12345678));
  return 0;
}
