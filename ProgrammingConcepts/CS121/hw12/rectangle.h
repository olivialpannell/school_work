//  Olivia Pannell
//  rectangle.h
//  Program 12
//  Wednesday Lab

#ifndef rectangle_h
#define rectangle_h

#include <iostream>
#include <string>
#include "shape.h"
using namespace std;

class Rectangle : public Shape
{
private:
    double width;
    double height;
public:
    Rectangle();
    Rectangle(int, int, double, double);
    void setWidth(double);
    void setHeight(double);
    double calculateArea();
    void print();
};

#endif /* rectangle_h */
