//Olivia Pannell
//Assignment 2 Question 2
#include <stdio.h>
unsigned int extract (signed int x, int i)
{
  //find the first mask for x
  signed int mk1;
  mk1 = 0xFF;
  mk1 = mk1 << (i << 3);
  x = x & mk1;

  //shift to get the values needed to rightmost
  int a = 4 - i;
  x = x >> (a << 3);

  //shift to get the sign extension
  x = x << 24;
  x = x >> 24;


  return x;

}
int main()
{
  printf("extract(0x12345678, 0): %x\n", extract(0x12345678, 0));
  printf("extract(0xABCDEF00, 2): %x\n", extract(0xABCDEF00, 2));

  return 0;

}
