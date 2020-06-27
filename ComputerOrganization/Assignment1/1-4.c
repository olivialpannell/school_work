// Olivia Pannell
// Assignment 1- Question 4
#include <stdio.h>
void printBytes(unsigned char *start, int len) {
 for (int i = 0; i < len; ++i) {
 printf(" %.2x", start[i]);
 }
 printf("\n");
}
void printInt(int x)
{
  printf("Int: ");
  printBytes((unsigned char *) &x, sizeof(int));
}
void printFloat(float x)
{
  printf("Float: ");
  printBytes((unsigned char *) &x, sizeof(float));

}
void printShort(short x)
{
  printf("Short: ");
  printBytes((unsigned char *) &x, sizeof(short));
}
void printLong(long x)
{
  printf("Long: ");
  printBytes((unsigned char *) &x, sizeof(long));
}
void printDouble(double x)
{
  printf("Double: ");
  printBytes((unsigned char *) &x, sizeof(double));
}
int main()
{
  int t1 = 5;
  float t2 = 5;
  short t3 = 5;
  long t4 = 5;
  double t5 = 5;
  printInt(t1);
  printFloat(t2);
  printShort(t3);
  printLong(t4);
  printDouble(t5);
}

/*  The thing that I noticed from my output is that it prints
out however many bytes there are based on the type. So int is 4,
float is 4, short is two, long and double are eight bytes.
The unexpected thing I noticed was the different byte patterns
between float and double compared to the rest. 
 */
