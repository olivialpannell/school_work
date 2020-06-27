// Olivia Pannell
// Assignment 1- Question 2
#include <stdio.h>
unsigned int replace (unsigned int x, int i, unsigned char b)
{
  //find the first mask for x
  unsigned int mk1, mk2;
  mk1 = 0xFF << (i << 3);
  //get the opposite of 00FF0000
  mk1 = ~mk1;
  x = x & mk1;

  //do the same for b to find my second mask
  mk2 = b << (i << 3);

  //combine the two
  return x | mk2;

}

int main()
{
  printf("replace(0x12345678, 2, 0xAB): %x\n", replace(0x12345678, 2, 0xAB));
  printf("replace(0x12345678, 0, 0xAB): %x\n", replace(0x12345678, 0, 0xAB));

  return 0;
}
