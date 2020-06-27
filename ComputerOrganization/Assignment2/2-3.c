//Olivia Pannell
//Assignment 2 Question 3
#include <stdio.h>

int le(float x, float y) {
 unsigned int ux = *((unsigned int*) &x); // convert x raw bits
 unsigned int uy = *((unsigned int*) &y); // convert y raw bits
 unsigned int sx = ux >> 31; // extract sign bit of ux
 unsigned int sy = uy >> 31; // extract sign bit of uy
 ux <<= 1; // drop sign bit of ux
 uy <<= 1; // drop sign bit of uy

 //sets sign variables equal to 1 or 0;
 int sign1 = (sx >= sy);
 int sign2 = (x <= uy);
 int sign3 = (sx == 1);
 int sign4 = (ux >= y);

 return ((sign1 & sign2) | (sign3 & sign4));
}
int main()
{
  printf("le(0.0f, 0.0f): %x\n", le(0.0f, 0.0f));
  printf("le(-0.0f, 0.0f): %x\n", le(-0.0f, 0.0f));
  printf("le(-1.0f, -1.0f): %x\n", le(-1.0f, -1.0f));
  printf("le(1.0f, 1.0f): %x\n", le(1.0f, 1.0f));
  printf("le(-1.0f, 0.0f): %x\n", le(-1.0f, 0.0f));
  printf("le(0.0f, 1.0f): %x\n", le(0.0f, 1.0f));
  printf("le(1.0f, 0.0f): %x\n", le(1.0f, 0.0f));
  printf("le(0.0f, -1.0f): %x\n", le(0.0f, -1.0f));

  return 0;
}
