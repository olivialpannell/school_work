//Olivia Pannell
//Assignment 4 Question 3
#include <stdio.h>

/*
C:
void transpose(array_t a) {
 for (long i = 0; i < N; ++i) {
 for (long j = 0; j < i; ++j) {
 long t1 = a[i][j];
 long t2 = a[j][i];
 a[i][j] = t2;
 a[j][i] = t1;
 }
 }
}

Assembly:
.L3:
movq (%rax), %rcx     // saving t1 into temp1 register
movq (%rdx), %rsi     // saving t2 into temp2 register
movq %rsi, (%rax)     // temp2 register into t2
movq %rcx, (%rdx)     // temp1 register into t1
addq $8, %rax         // finding the ith column and adding it to t2
                      // OR increasing the counter i by another column??
addq $32, %rdx        // finding the ith row and adding to t1
cmpq %r9, %rax        // comparing j and i
jne .L3               // jumping if not equal
*/


#define N 4
typedef long array_t[N][N];
void transpose(array_t a)
{
  long *aptr = *a;  //pointer to start of a
  long *irow, *icol; //initialize pointers for ith column/row

  for (long i = 0; i < N; ++i)
  {
    //icol = &a[0][i]; //sets icol to the ith column of a
    //irow = &a[i][0]; //sets irow to the ith row of a
    for (long j = 0; j < i; ++j)
    {
      long temp;  //temp for swapping later
      icol = aptr + (j * N);  //finding the column
      icol += i;              //indexing it to exact position
      irow = aptr + (i * N);  //finding the row
      irow += j;              //indexing to exact position

      //swapping the two values
      temp = *irow;
      *irow = *icol;
      *icol = temp;
    }
  }
}

int main()
{
  array_t arr = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
  transpose(arr);

  return 0;
}
