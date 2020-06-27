//  Olivia Pannell
//  circle.h
//  Program 12
//  Wednesday Lab

#ifndef circle_h
#define circle_h
#include <iostream>
#include <string>
#include "shape.h"
using namespace std;

class Circle: public Shape
{
private:
    double radius;
public:
    Circle();
    Circle(int, int, double);
    void setRadius(double);
    double calculateArea();
    void print();
};

#endif /* circle_h */
