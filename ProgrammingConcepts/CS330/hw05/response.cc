//
// Implementation of methods for classes Response, AngryResponse, HappyResponse
//
#include <iostream>
#include <string>
#include <algorithm>

#include "response.hh"

using namespace std;

//
// Implementation of Word methods
//
// Don't worry too hard about these implementations.
// If you'd like to learn more about STL see: https://www.geeksforgeeks.org/the-c-standard-template-library-stl/
//
string Word::upper()
{
  string result(theWord);
  transform(result.begin(), result.end(), result.begin(), ::toupper);
  return result;
}

string Word::lower()
{
  string result(theWord);
  transform(result.begin(), result.end(), result.begin(), ::tolower);
  return result;
}

//
// Implementation of Response methods
//
bool Response::checkAndRespond(const string &inWord, ostream &toWhere)
{
  // This method should check if its object's keyword is in the inWord message.
  // If it is, the method should call the  `respond` method passing the toWhere stream and return true.
  // If it isn't, the method should return false.


  // compares the uppercase keyword to the length by using find
  // if greater than length the word is not found and returns false
  if(inWord.find(keyword.upper()) < inWord.length())
  {
    respond(toWhere);
    return true;
  }
  return false;

}

void Response::respond(ostream &toWhere)
{
  // Prints out response
  toWhere << response << endl;

}


//
// Implementation of AngryReponse methods
//

void AngryResponse::respond(ostream &toWhere)
{
  // Prints out response and an angry face
  toWhere << response << endl;
  toWhere << " >:( " << endl;

}

//
// Implementation of HappyResponse methods
//
void HappyResponse::respond(ostream &toWhere)
{
  // Prints out response and a happy face
  toWhere << response << endl;
  toWhere << " ;) " << endl;

}

