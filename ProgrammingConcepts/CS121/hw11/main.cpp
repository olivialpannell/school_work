//  Olivia Pannell
//  main.cpp
//  Program 11
//  CPSC 121-23

#include <iostream>
#include <string>
#include <fstream>
#include "DogArray.h"
using namespace std;

int main()
{
    string txtFile;
    DogArray d1; //dog one, dog two
    Dog s1, s2, s3; //struct
    char ch;
    
    cout << "Enter the name of the input file: ";
    getline(cin, txtFile);
    
    
    ifstream fin(txtFile); 
    
    //opens file
    if (!fin.is_open())
    {
        cout << "File cannot open. ";
        return 1;
    }
    
    //reads in file
    while(fin >> ch)
    {
        fin.putback(ch);
        getline(fin, s1.breed);
        fin >> s1.age;
        fin >> s1.weight;
        d1 += s1;
    }
    
    //writes out data size and array size
    cout << endl;
    cout << "Number of Dogs: " << d1.getdSize() << endl;
    cout << "Array size: " << d1.getaSize() << endl;
    cout << endl;
    
    // writes out just 5 element
    s1 = d1.operator[](4);
    cout << "Fifth element: " << s1.breed << " " << s1.age;
    cout << " "	<< s1.weight << endl << endl;
    
    cout << "Original Array" << endl;
    cout << d1;
    
    // copy constructor
    DogArray d2=d1;
    s2.breed = "Keltie";
    s2.age = 3;
    s2.weight = 48.7;
    d2.operator[](0) = s2;
    cout << "Altered array from copy constructor" << endl;
    cout << d2;
    
    // uses = operator
    DogArray d3;
    d3.operator=(d1);
    s3.breed = "Akita";
    s3.age = 7;
    s3.weight = 99.9;
    d1.operator[](1) = s3;
    cout << "Altered array from copy operator" << endl;
    cout << d2;
    
    //sorts by abc
    cout << "Sorted alphabetically by breed";
    d1.operator=(d3);
    cout << endl;
    d2.sortAlpha();
    cout << d2;
    
    //sort by weight
    cout << "Sorted by weight (large to small)";
    d1.operator=(d3);
    cout << endl;
    d2.sortWeight();
    cout << d2;
    
    
    return 0;
}
