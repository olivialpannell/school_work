//Olivia Pannell
//Assignment 3 Question 2
#include <stdio.h>

long f(long a, long b, long c)
{
  long temp;
  temp = b + c;
  temp = temp * a;
  temp = temp ^ (temp << 63);
  temp = temp ^ (temp >> 63);
  return temp;
}

int main()
{
  printf("f(1, 2, 4): %ld\n", f(1, 2, 4));
  printf("f(3, 5, 7): %ld\n", f(3, 5, 7));
  printf("f(10, 20, 30): %ld\n", f(10, 20, 30));
  return 0;
}
