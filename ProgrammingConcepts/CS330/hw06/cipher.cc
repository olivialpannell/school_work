#include "cipher.h"

#define UPPER_CASE(r) ((r) - ('a' - 'A'))

struct Cipher::CipherCheshire {
    string cipherText;
};

Cipher::Cipher()
{
    smile = new CipherCheshire;
    smile->cipherText = "abcdefghijklmnopqrstuvwxyz ";
}
Cipher::Cipher(string in)
{
    smile = new CipherCheshire;
    smile->cipherText = in;
}
string Cipher::encrypt(string raw)
{
    string retStr;
    cout << "Encrypting..." << endl;
    for(unsigned int i = 0; i < raw.size(); i++) {
        unsigned int pos;
        bool upper = false;
        if(raw[i] == ' ') {
            pos = 26;
        } else if(raw[i] >= 'a') {
            pos = raw[i] - 'a';
        } else {
            pos = raw[i] - 'A';
            upper = 1;
        }
        if(upper) {
            retStr += UPPER_CASE(smile->cipherText[pos]);
        } else {
            retStr += smile->cipherText[pos];
        }
    }
    cout  << "Done" << endl;

    return retStr;
}

string Cipher::decrypt(string enc)
{
    string retStr;
    cout << "Decrpyting..." << endl;

    for(unsigned int i = 0; i < enc.size(); i++)
    {
        for(unsigned int j = 0; j < smile->cipherText.size(); j++)
        {
            unsigned int pos;
            bool upper = false;

            // Change to lower case during testing
            // but save that it is an uppercase
            if(enc[i] < 'a')
            {
                upper = true;
                enc[i] = enc[i] + ('a' - 'A');
            }

            // Find the matching letter
            if(enc[i] == smile->cipherText[j])
            {
                // Find what the real value is by adding ascii value a
                // Then adds it to the string by its ascii value
                // Takes into account the the space will always equal '{'
                pos = j + 'a';
                if(pos == '{')
                {
                    retStr += " ";
                }
                else if(upper){
                    retStr += UPPER_CASE(pos);
                } 
                else {
                 retStr += pos;
                }
            }   
        }
    }
    cout << "Done" << endl;

    return retStr;
}




struct CaesarCipher::CaesarCipherCheshire : CipherCheshire {
     int rot;
};

CaesarCipher::CaesarCipher()
{
    CaesarSmile = new CaesarCipherCheshire;
    CaesarSmile->cipherText = "abcdefghijklmnopqrstuvwxyz ";
    CaesarSmile->rot = 0;
} 

CaesarCipher::CaesarCipher(string in, int rot)
{
    CaesarSmile = new CaesarCipherCheshire;
    CaesarSmile->cipherText = in;
    CaesarSmile->rot = rot % 27;
}

string CaesarCipher::encrypt(string raw)
{
    string retStr;
    cout << "Encrypting..." << endl;

    // Similiar to the Encrypt from above but adds the offset
    // as well as makes the string 'circular'
    for(unsigned int i = 0; i < raw.size(); i++) {
        unsigned int pos;
        bool upper = false;
        if(raw[i] == ' ') {
            pos = 26 + CaesarSmile->rot;
            //make it circular
            if(pos > 26)
            {
                pos = pos % 27;
            }
        } else if(raw[i] >= 'a') {
            pos = raw[i] - 'a' + CaesarSmile->rot;
            //make it circular
            if(pos > 26)
            {
                pos = pos % 27;
            }
        } else {
            pos = raw[i] - 'A' + CaesarSmile->rot;
            upper = 1;
            //make it circular
            if(pos > 26)
            {
                pos = pos % 27;
            }
        }
        if(upper) {
            retStr += UPPER_CASE(CaesarSmile->cipherText[pos]);
        } else {
            retStr += CaesarSmile->cipherText[pos];
        }
    }

    cout << "Done" << endl;

    return retStr;

}

string CaesarCipher::decrypt(string enc)
{
    string retStr;
    cout << "Decrpyting..." << endl;
    // Fill in code here
    for(unsigned int i = 0; i < enc.size(); i++)
    {
        unsigned int pos;
        bool upper = false;
        for(unsigned int j = 0; j < CaesarSmile->cipherText.size(); j++)
        {
 
            // Change to lower  and update upper
            if(enc[i] < 'a' && enc[i] != ' ')
            {
                upper = true;
                enc[i] = enc[i] + ('a' - 'A');
            }
            // If it found the matching code
            if(enc[i] == CaesarSmile->cipherText[j])
            {
                // Decrypt and take into count the offset by subtracting j from it
                int tempj = CaesarSmile->rot - j;
                tempj = 27 - tempj;
                if(tempj > 26)
                {
                    tempj = tempj % 27;
                }
                pos = tempj + 'a';

                // If pos is a space add it to the string
                if((pos < 'a' && pos > 'Z') || pos > 'z' || pos < 'A')
                {
                    retStr += " ";
                    break;
                }
                // If upper was triggered up above
                else if(upper){
                    retStr += UPPER_CASE(pos);
                    break;
                } 
                else {
                    retStr += pos;
                    break;
                }

            }   
        }
    }

    cout << "Done" << endl;

    return retStr;
}
CaesarCipher CaesarCipher::operator++()
{
    CaesarSmile->rot++;
    return *this;
}
CaesarCipher CaesarCipher::operator--()
{
    CaesarSmile->rot --;
    return *this;
}



