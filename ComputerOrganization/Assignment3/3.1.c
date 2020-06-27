//Olivia Pannell
//Assignment 3 Question 1
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
 int length;
 int *dataPtr;
} IntArray;
IntArray* mallocIntArray(int length)
{
  IntArray* arr = (IntArray*)malloc(sizeof(IntArray));
  arr->dataPtr = malloc(length * sizeof(int));
  return arr;
}
void freeIntArray(IntArray *arrayPtr)
{
  free(arrayPtr->dataPtr);
  free(arrayPtr);
}
void readIntArray(IntArray *array)
{
  char *userInput;
  char *endptr;
  long result;
  int number = 0;

  //goes length times and adds to dataPtr
  for(int i = 0; i < array->length; i++)
  {

    printf("Enter int: ");
    scanf("%s", userInput);
    result = strtol(userInput, &endptr, 10);
    //error checking
    if (result == 0)
    {
      printf("Invaild Input! Try Again. \n");
      //does not count towards the count in for loop
      i--;
    }
    else
    {
      number = (int)result;
      array->dataPtr[i] = number;
    }
  }
}
void swap(int *xp, int *yp)
{
  //creates temp and swaps
  int temp;
  temp = *xp;
  *xp = *yp;
  *yp = temp;
}
void sortIntArray(IntArray *array)
{
  //https://www.geeksforgeeks.org/bubble-sort/
  int i, j;
   for (i = 0; i < array->length-1; i++)
       for (j = 0; j < array->length-i-1; j++)
           if (array->dataPtr[j] > array->dataPtr[j+1])
              swap(&array->dataPtr[j], &array->dataPtr[j+1]);

}
void printIntArray(IntArray *array)
{
  printf("[ " );
  for(int i = 0; i < array->length; i++)
  {
    printf("%d ", array->dataPtr[i]);
  }
  printf("] \n");
}
int main()
{
  char *userInput;
  char *endptr;
  long result;
  int length = 0;


  //infinite loop until a valid input
  while(1)
  {
    //ask for length and changes it into long
    printf("Enter a length: ");
    scanf("%s", userInput);
    result = strtol(userInput, &endptr, 10);

    //error checking
    if (result == 0)
    {
      printf("Invaild Input! Try Again. \n");
    }
    else if(result < 0)
    {
      printf("Invalid Input! Try a positive number.\n");
    }
    else
    {
      //turn results into an int and exit the loop
      length = (int)result;
      break;
    }
  }

  IntArray *arr = mallocIntArray(length);
  arr->length = length;
  printf("\n");

  //call functions
  readIntArray(arr);
  sortIntArray(arr);
  printIntArray(arr);
  freeIntArray(arr);

  return 0;
}
