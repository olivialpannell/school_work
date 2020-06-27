// Olivia Pannell
// Wednesday Lab
// Program 13
// circle.h

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
#include "shape.h"

#ifndef circle_h
#define circle_h

class Circle : public Shape
{
private:
    double radius;
public:
    Circle();
    Circle(int x, int y, double r);
    double setRadius(double r);
    virtual void print();
    virtual double calcArea();
};

#endif
