//Olivia Pannell
//Assignment 6 Question 1
#include <stdio.h>

int f(int a, int b, int c, int d, int n) {
	 int result = 0;
	 int ab = a * b;
	 int cd = c * d;
	 for (int i = 0; i < n; ++i) 
	 {
	 	int cdi = cd *w i;
		 for (int j = 0; j < n; ++j) 
		 {
		 result += ab + cdi + j;
		 }
	 }
	 return result;
}
int main()
{
	printf("f(1, 2, 3, 4, 5): %d \n", f(1, 2, 3, 4, 5));
	printf("f(2, 3, 4, 5, 6): %d \n", f(2, 3, 4, 5, 6));
	printf("f(6, 5, 4, 3, 2): %d \n", f(6, 5, 4, 3, 2));
	printf("f(5, 4, 3, 2, 1): %d \n", f(5, 4, 3, 2, 1));
	return 0;
}