//  Olivia Pannell
//  DogArray.cpp
//  Program 11
//  CPSC 121-23

#include <iostream>
#include <string>
#include <iomanip>
#include "DogArray.h"
using namespace std;

ostream & operator<<(ostream & out, const DogArray & s)
{
    for (int i = 0; i < s.numDogs; i++)
    {
        out << "Breed: " << setw(17) << left << s.dArray[i].breed << setw(13)
        << right << "Age: " << setw(3) << right << s.dArray[i].age
        << setw(13) << right << "Weight: " << s.dArray[i].weight;
        out << endl;
    }
    out << endl;
    return out;
}
// sets array size to 5
DogArray::DogArray(int asize)
{
    arraySize = (asize < 0) ? asize : 5;
    numDogs = 0;
    dArray = new Dog[arraySize];
}
//checks for correct size
DogArray::DogArray(const DogArray & a)
{
    arraySize = a.arraySize;
    numDogs = a.numDogs;
    dArray = new Dog[arraySize];
    for (int i = 0; i < numDogs; i++)
        dArray[i] = a.dArray[i];
}
// destructor
DogArray::~DogArray()
{
    delete []dArray;
}

int DogArray::getaSize()
{
    return arraySize;
}
int DogArray::getdSize()
{
    return numDogs;
}
//sorts
void DogArray::sortAlpha()
{
    int maxPos;
    for (int curTop = 0; curTop < numDogs - 1; curTop++)
    {
        maxPos = curTop;
        for (int indx = curTop + 1; indx < numDogs; indx++)
        {
            if (dArray[indx].breed < dArray[maxPos].breed)
            {
                maxPos = indx;
            }
        }
        if (maxPos != curTop)
            swap(dArray[maxPos], dArray[curTop]);
    }
}
//sorts
void DogArray::sortWeight()
{
    int maxPos;
    for (int curTop = 0; curTop < numDogs - 1; curTop++)
    {
        maxPos = curTop;
        for (int indx = curTop + 1; indx < numDogs; indx++)
        {
            if (dArray[indx].weight > dArray[maxPos].weight)
            {
                maxPos = indx;
            }
        }
        if (maxPos != curTop)
            swap(dArray[maxPos], dArray[curTop]);
    }
}
DogArray DogArray:: operator=(DogArray other)
{
    if (this != &other)
    {
        delete[] dArray;
        arraySize = other.arraySize;
        numDogs = other.numDogs;
        dArray = new Dog[arraySize];
        for (int i = 0; i < numDogs; i++)
            dArray[i] = other.dArray[i];
    }
    return *this;

}

Dog & DogArray:: operator[](int a)
{
    if (a >= 0 && a < numDogs)
        return dArray[a];
    cout << "Subscript not legal.";
    exit(1);
}
DogArray DogArray:: operator+=(Dog a)
{
    if (arraySize == numDogs)
    {
        Dog* temp;
        temp = new Dog[arraySize * 2];
        
        for (int i = 0; i < numDogs; i++)
        {
            temp[i] = dArray[i];
        }
        
        delete[] dArray;
        dArray = temp;
        temp = NULL;
        arraySize = arraySize * 2;
    }
    dArray[numDogs] = a;
    numDogs++;
    return *this;

}
