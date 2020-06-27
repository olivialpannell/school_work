// Olivia Pannell
// CPSC 121-23
// Program #6

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

struct PurchaseRecord
{
    string name;
    int num;
    double totalCost;
    double costs[8];
};

void getData(ifstream & fin, PurchaseRecord a[], int & dsize);
void calcTotals(PurchaseRecord a[], int dsize);
void sortCosts(double a[], int dsize);
void sortNames(PurchaseRecord a[], int dsize);
void sortTotalCosts(PurchaseRecord a[], int dsize);
void output(PurchaseRecord a[], int dsize);
void nameSearch();

int main()
{
    PurchaseRecord a[10];
    
    string txtFile;
    
    cout << "Enter the name of the input file: ";
    getline(cin, txtFile);
    
    
    ifstream fin(txtFile);
    
    if (!fin.is_open())
    {
        cout << "Not found ";
        return 1;
    }
    
    //char ch;
    int dsize = 0;
    
    
    getData(fin, a, dsize);
    calcTotals(a, dsize);
    
    for (int i = 0; i <= dsize; i++)
    {
        sortCosts(a[i].costs, dsize);
        
    }
    sortNames(a, dsize);
    sortTotalCosts(a, dsize);
    output(a, dsize);
    nameSearch();
    
    dsize++;
    
    
    return 0;
}

void getData(ifstream & fin, PurchaseRecord a[], int& dsize)
{
    char ch;
    while (dsize < 10 && fin >> ch)
    {
        fin.putback(ch);
        getline(fin, a[dsize].name);
        fin >> a[dsize].num;
        
        for (int i = 0; i < a[dsize].num; i++)
        {
            fin >> a[dsize].costs[i];
        }
    }
}

void calcTotals(PurchaseRecord a[], int dsize)
{
    double sum = 0;
    
    for (int i = 0; i < a[dsize].num; i++)
    {
        sum += a[dsize].costs[i];
    }
    a[dsize].totalCost = sum;
}

void sortCosts(double a[], int dsize)
{
    int maxPos;
    for (int curTop = 0; curTop < dsize - 1; curTop++)
    {
        maxPos = curTop;
        for (int indx = curTop + 1; indx < dsize; indx++)
        {
            if (a[indx] < a[maxPos])
            {
                maxPos = indx;
            }
        }
        if (maxPos != curTop)
            swap(a[maxPos], a[curTop]);
    }
}

void sortNames(PurchaseRecord a[], int dsize)
{
    int minPos;
    for (int curTop = 0; curTop <= dsize - 1; curTop++)
    {
        minPos = curTop;
        for (int indx = curTop + 1; indx < dsize; indx++)
        {
            if (a[indx].name < a[minPos].name)
            {
                minPos = indx;
            }
        }
        if (minPos != curTop)
            swap(a[minPos].name, a[curTop].name);
    }
}

void sortTotalCosts(PurchaseRecord a[], int dsize)
{
    int maxPos;
    for (int curTop = 0; curTop < dsize - 1; curTop++)
    {
        maxPos = curTop;
        for (int indx = curTop + 1; indx < dsize; indx++)
        {
            if (a[indx].totalCost < a[maxPos].totalCost)
            {
                maxPos = indx;
            }
        }
        if (maxPos != curTop)
            swap(a[maxPos].totalCost, a[curTop].totalCost);
    }
}

void nameSearch()
{
    
}

void output(PurchaseRecord a[], int dsize)
{
    cout << a[dsize].name << ", " << a[dsize].num << " purchases for a total of "
    << a[dsize].totalCost << endl;
    
    cout << "\t";
    
    for (int i = 0; i < a[dsize].num; i++)
    {
        cout << a[dsize].costs[i] << " ";
    }
    
    cout << endl;
}
