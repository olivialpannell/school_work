//  Olivia Pannell
//  main.cpp
//  Program 12
//  Wednesday Lab

#include <iostream>
#include "shape.h"
#include "circle.h"
#include "rectangle.h"
using namespace std;

int main()
{
    Shape one, two(3, 5, "Triangle");
    one.print();
    cout << endl;
    two.print();
    cout << endl;
    one.setLocation(4, 6);
    one.print();
    cout << endl << endl;
    
    Circle three, four(2, 5, 4.2);
    three.print();
    four.print();
    three.setLocation(3,3);
    three.setRadius(6.5);
    three.print();
    cout << endl;
    
    Rectangle five, six(5,4,3.2,1);
    five.print();
    six.print();
    five.setLocation(2, 2);
    five.setHeight(5.0);
    five.setWidth(4.0);
    five.print();
    cout << endl;

    Shape *sptr1, *sptr2, *sptr3;
    sptr1 -> print();
    cout << endl;
    sptr2 -> print();
    cout << endl;
    sptr3 -> print();
    cout << endl;
    
    return 0;
}
