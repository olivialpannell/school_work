// Olivia Pannell
// CPSC 121-23
// Program 9


#include <iostream>
using namespace std;
#include "purchase.h"

int main()
{
    Purchase one, two(3,12.997);
    one.print();
    two.print();
    if(true)
    {
        Purchase three(8,12.1275);
        three.print();
    }
    Purchase four(5,9);
    four.print();
    
    one.setNumItems(12);
    one.setItemPrice(2.99);
    cout << "one items: " << one.getNumItems() << endl;
    cout << "one price: " << one.getItemPrice() << endl;
    one.print();
    
    
    return 0;
}
