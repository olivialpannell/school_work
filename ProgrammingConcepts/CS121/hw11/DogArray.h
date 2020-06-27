//  Olivia Pannell
//  DogArray.h
//  Program 11
//  CPSC 121-23
#ifndef DogArray_h
#define DogArray_h

#include <iostream>
#include <string>
using namespace std;

struct Dog
{
    string breed;
    int age;
    double weight;
};
class DogArray
{
    friend ostream & operator<<(ostream &, const DogArray &);
private:
    int numDogs;
    int arraySize;
    Dog * dArray; //pointer to dog array
public:
    DogArray(int asize = 5);
    DogArray(const DogArray & a);
    ~DogArray();
    int getaSize(); //gets array size
    int getdSize(); //gets data size
    void sortAlpha(); //sorts alphabetically
    void sortWeight(); //sorts by weight
    DogArray operator=(DogArray);
    Dog& operator[](int);
    DogArray operator+=(Dog);
};



#endif /* DogArray_h */
