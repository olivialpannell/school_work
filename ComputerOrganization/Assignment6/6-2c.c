//Olivia Pannell
//Assignment 6 Question 2c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void inner(float *u, float *v, int length, float *dest) {
	 int i;
	 float sum = 0.0f;
	 for (i = 0; i < length; ++i) {
		sum += u[i] * v[i];
	 }
	 *dest = sum;
} 

void inner2(float *u, float *v, int length, float *dest) {
	 float sum = 0.0f;
	 int newlength = length - 3;
	 float a, b, c;
	 a = 0.0f;
	 b = 0.0f;
	 c = 0.0f;
	 int i;
	 //change i++ to i+= 4 since four-way
	 for (i = 0; i < newlength; i+=4) 
	 {
	 	//unrolling here
		sum += u[i] * v[i];
		a = a + (u[i+1] * v[i+1]);
		b = b + (u[i+2] * v[i+2]);
		c = c + (u[i+3] * v[i+3]);
	 }
	 //if not divisible by 4 get whatever is left by using i 
	 for (int j = i; j < length; j++)
	 {
	 	sum += u[j] * v[j];
	 }

	 //add all together and set dest equal to it
	 *dest = sum + a + b + c;
} 

//took from 6-3 to create an array and test the times
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
	//creates arrays of random numbers of size
	int size = 150000;
	float *arr1 = createArray(size);
	float *arr2 = createArray(size);


	// mallocs the destination
	float *destin = (float *)malloc(size * sizeof(float));
	float *destin2= (float *)malloc(size * sizeof(float));

	//measure inner function 
	clock_t start = clock();

	inner(arr1, arr2, size, destin);

	clock_t end = clock();
	double run_time = (double)(end - start) / CLOCKS_PER_SEC;
	printf("inner took: %lf \n", run_time);

	//measure inner2 function
	clock_t newstart = clock();

	inner2(arr1, arr2, size, destin2);

	clock_t newend = clock();
	double newrun_time = (double)(newend - newstart) / CLOCKS_PER_SEC;
	printf("inner2 took: %lf \n", newrun_time);

	//free arrays
	free(destin);
	free(destin2);
	free(arr1);
	free(arr2);

	return 0;
}