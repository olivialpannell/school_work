// Olivia Pannell
// Program 8
// CPSC 121-23

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

// Array maximum sizes
const int SPENDING_ARRAY_SIZE = 20;
const int COST_ARRAY_SIZE = 8;

// The struct type for each person
struct SpendingRecord
{
    string name;
    int numPurch;
    double totalCost;
    double purchase[COST_ARRAY_SIZE];
};

void getData(ifstream&, SpendingRecord[], int & dsize);
void calcTotal(SpendingRecord[], int dsize);
void sortPurchases(double [], int psize);
void sortByName(SpendingRecord[], int dsize);
void sortByTotal(SpendingRecord[], int dsize);
void findAName(SpendingRecord[], int dsize, string);
void print(SpendingRecord[], int dsize);


int main()
{
    SpendingRecord srArr[SPENDING_ARRAY_SIZE];
    int datasize;
    string searchname;
    string filename;
    ifstream fin;
    
    cout << fixed << setprecision(2);
    
    cout << "Enter name of input file: ";
    cin >> filename;
    cin.ignore(100,'\n');
    fin.open(filename.c_str());
    if(!fin)
    {
        cout << "File not found" << endl;
        return 1;
    }
    cout << endl;
    
    getData(fin, srArr, datasize);
    for(int i=0; i<datasize; i++)
        sortPurchases(srArr[i].purchase, srArr[i].numPurch);
    calcTotal(srArr, datasize);
    sortByTotal(srArr, datasize);
    print(srArr, datasize);
    cout << endl;
    sortByName(srArr, datasize);
    print(srArr, datasize);
    cout << endl << "Enter a name to find: ";
    getline(cin, searchname);
    findAName(srArr, datasize, searchname);
    
    fin.close();
    return 0;
}

// function getData - receives an open file and reads in SpendingRecord data
//     into an array.  Brings back the file data and the count.
void getData(ifstream & fin, SpendingRecord sArr[], int & dsize)
{
    char ch;
    dsize = 0;
    while(dsize < SPENDING_ARRAY_SIZE && fin >> ch)
    {
        fin.putback(ch);
        getline(fin,sArr[dsize].name);
        fin >> sArr[dsize].numPurch;
        for(int i=0; i<sArr[dsize].numPurch; i++)
            fin >> sArr[dsize].purchase[i];
        dsize++;
    }
}
// function calcTotal - receives an array of SpendingRecords and the
//     data size.  Calculates and stores the total for each element.
void calcTotal(SpendingRecord sArr[], int dsize)
{
    for(int rec = 0; rec < dsize; rec++)
    {
        sArr[rec].totalCost = 0.0;
        for(int pch = 0; pch < sArr[rec].numPurch; pch++)
        {
            sArr[rec].totalCost += sArr[rec].purchase[pch];
        }
    }
}
// function sortPurchases - receives an array of doubles and sorts them
//     into descending order
void sortPurchases(double arr[], int psize)
{
    int maxPos;
    for(int curTop = 0; curTop < psize-1; curTop++)
    {
        maxPos = curTop;
        for(int indx = curTop + 1; indx < psize; indx++)
        {
            if(arr[indx] > arr[maxPos])
            {
                maxPos = indx;
            }
        }
        if(maxPos != curTop)
            swap(arr[maxPos], arr[curTop]);
    }
}
// function sortByName - receives an array of SpendingRecords and sorts
//     them into ascending order by name field.
void sortByName(SpendingRecord sArr[], int dsize)
{
    int minPos;
    for(int curTop = 0; curTop < dsize-1; curTop++)
    {
        minPos = curTop;
        for(int indx = curTop + 1; indx < dsize; indx++)
        {
            if(sArr[indx].name < sArr[minPos].name)
            {
                minPos = indx;
            }
        }
        if(minPos != curTop)
            swap(sArr[minPos], sArr[curTop]);
    }
}
// function sortByTotal - receives an array of SpendingRecords and sorts
//     them into descending order by totalCost field.
void sortByTotal(SpendingRecord sArr[], int dsize)
{
    int maxPos;
    for(int curTop = 0; curTop < dsize-1; curTop++)
    {
        maxPos = curTop;
        for(int indx = curTop + 1; indx < dsize; indx++)
        {
            if(sArr[indx].totalCost > sArr[maxPos].totalCost)
            {
                maxPos = indx;
            }
        }
        if(maxPos != curTop)
            swap(sArr[maxPos], sArr[curTop]);
    }
}
// function findAName - receives an array of SpendingRecords and a search
//     string.  Writes out the smallest and largest expenses if the name
//     is found or a "not found" message if it is not in the data.
void findAName(SpendingRecord sArr[], int dsize, string nameToFind)
{
    for(int i = 0; i < dsize; i++)
    {
        if(sArr[i].name == nameToFind)
        {
            cout << sArr[i].name << " " << sArr[i].totalCost << " " << endl
            << "  Largest and smallest purchases: " << sArr[i].purchase[0]
            << ", " << sArr[i].purchase[sArr[i].numPurch-1] << endl;
            return;
        }
    }
    cout << nameToFind << " was not found in the data" << endl;
}
// function print - receives an array of SpendingRecords and writes them out
//     following a given format.
void print(SpendingRecord sArr[], int dsize)
{
    int numP;
    for(int rec = 0; rec < dsize; rec++)
    {
        numP = sArr[rec].numPurch;
        cout << sArr[rec].name << ", " << numP << " purchases for a total of "
        << sArr[rec].totalCost << endl;
        cout << "  ";
        for(int p=0; p<numP; p++)
            cout << sArr[rec].purchase[p] << " ";
        cout << endl;
    }
}
