//
//  main.cpp
//  reverseString
//
//  Created by Marcelo Cunha de Azambuja on 6/10/19.
//  Copyright © 2019 Marcelo Cunha de Azambuja. All rights reserved.
//

#include <iostream>

using namespace std;

int main(){
    string str;
    int i, sizeString;
    char newChar;
    
    cout << "Enter string: ";
    getline(cin, str);
    
    sizeString=str.size();
    
    cout << "Size of your string: " << sizeString << endl;
    
    for (i=0; i<sizeString; i++)
        cout << str[i];
    
    cout << endl;
    
    cout << "== Now the string reversed whithou any built-in method: \n";
    
    for (i=sizeString;i>=0;i--)
        cout << str[i];
    
    cout << endl;
    
    cout << "== Now the string reversed using built-in methods: \n";
    
    
    // Declaring reverse iterator
    std::string::reverse_iterator it1;
    
    //rbegin(): this function returns a reverse iterator pointing at the end of string.
    for (it1=str.rbegin(); it1!=str.rend(); it1++)
        cout << *it1;
    
    //Using push_back() function to input a new char at the end of a string
    
    cout << "\n\nEnter a new char: ";
    newChar=getchar();
    
    str.push_back(newChar);
    
    cout << "String after new char: " << str << "\n\n";
    
    return 0;
}
