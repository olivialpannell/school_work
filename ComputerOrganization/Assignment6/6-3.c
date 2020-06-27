//Olivia Pannell
//Assignment 6 Question 3
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float f(float *a, int n) {
	float prod = 1.0f;
	for (int i = 0; i < n; ++i) 
	{
		if (a[i] != 0.0f) 
		{
			prod *= a[i];
		}
	}
	return prod;
}
float g(float *b, int n)
{
	float prod = 1.0f;
	for (int i = 0; i < n; ++i) 
	{
		prod *= b[i];
	}
	return prod;
}

float* createArray(int size) {
	float *a = (float *)malloc(size * sizeof(float));
	for (int i = 0; i < size; ++i) {
		// 50% chance that a[i] is 0.0f, random value on the range
		// [0.76, 1.26] otherwise.
		float r = rand()/(float)RAND_MAX;
		a[i] = r < 0.5f ? 0.0f : r + 0.26f;
	}
	return a;
}

int main()
{
	float *a = createArray(10000);

	//free space for b
	float *b = (float *)malloc(10000);

	//counter for index of b
	int count = 0;

	//checking if element from a is 0 and if not insert to b
	for(int i = 0; i < 10000; i++)
	{
		if(a[i] != 0.0f)
		{
			b[count] = a[i];
			count += 1;
		}
	}

	//measure f(a)
	clock_t start = clock();

	float prod = f(a, 10000);

	clock_t end = clock();
	double run_time = (double)(end - start) / CLOCKS_PER_SEC;
	printf("f(a) took: %lf \n", run_time);

	//measure g(a)
	clock_t newstart = clock();

	//call function
	float newprod = g(b, count);

	clock_t newend = clock();
	double newrun_time = (double)(newend - newstart) / CLOCKS_PER_SEC;
	printf("g(b) took: %lf \n", newrun_time);

	//free memory
	free(a);
	free(b);

	return 0;
}