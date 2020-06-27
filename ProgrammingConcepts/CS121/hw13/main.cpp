// Olivia Pannell
// Wednesday Lab
// Program 13
// main.cpp

#include <iostream>
#include <string>
using namespace std;
#include "shape.h"
#include "rectangle.h"
#include "circle.h"

int main()
{
    Shape *ptrS1, *ptrS2, *ptrS3, *ptrS4, *ptrS5;
    Shape *shapearr[5] = {ptrS1 = NULL, ptrS2 = NULL,
        ptrS3 = NULL, ptrS4 = NULL, ptrS5 = NULL };
    
    string shape;
    for (int i = 0; i < 5; i++)
    {
        cout << "Create a rectangle or circle? ";
        cin >> shape;
        
        while (shape != "rectangle" && shape != "Rectangle" &&
               shape != "circle" && shape != "Cirlce")
        {
            cout << "Invaild choice. Try again: ";
            cin >> shape;
        }
        if (shape == "circle" || shape == "Circle")
        {
            cout << "Enter a value for x, y, and the radius: ";
            
            int x;
            int y;
            double radius;
            
            cin >> x >> y >> radius;
            
            Circle c(x, y, radius);
            shapearr[i] = new Circle(x, y, radius);
            
            cout << endl;
        }
        else if (shape == "rectangle" || shape == "Rectangle")
        {
            cout << "Enter a value for x, y, width and height: ";
            
            int x;
            int y;
            double width;
            double height;
            
            cin >> x >> y >> width >> height;
            
            Rectangle r(x, y, width, height);
            shapearr[i] = new Rectangle(x, y, width, height);
            
            cout << endl;
        }
    }
    
    for (int k = 0; k < 5; k++)
    {
        shapearr[k]->print();
        cout << endl;
        shapearr[k]->calcArea();
        //delete shapearr[k];
    }
    
    return 0;
}
