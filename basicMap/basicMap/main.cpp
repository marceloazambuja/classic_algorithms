//
//  main.cpp
//  basicMap
//
//  Created by: http://cs.stmarys.ca/~porter/csc/ref/stl/cont_map.html
//  *small changes by Marcelo Azambuja on 6/8/2019
//

#include <iostream>
#include <map>
using namespace std;

int main(){
    char whichKey;
    
    cout << "\nThis program creates an empty map, places three "
    "key/value pairs into it,\nthen displays the values by "
    "accessing them via their keys.";
    cout << "\nPress Enter to continue ... ";  cin.ignore(80, '\n');
                                            //ignores first 80 characters or all the character untill it encounters delimeter (here \n ), so it ignores until \n is encountered).
    
    map<char, int> m;
    if (m.empty())
        cout << "\nThe newly created map is currently empty.";
    
    cout << "\nPress Enter to continue ... ";  cin.ignore(numeric_limits<streamsize>::max(),'\n');
                                                    //other way to safely discard \n from the standard stream stdin.
    m['A'] = 65;
    m['B'] = 66;
    m['C'] = 67;
    
    cout << "\nAfter entering the three key/value pairs, the size of "
            "the map is now " << m.size() << ".";
    cout << "\nPress Enter to continue ... ";  cin.ignore(80, '\n');
    
    cout << "\nIf the component key is A, the component value is "
             << m['A'] << ".";
    cout << "\nIf the component key is B, the component value is "
             << m['B'] << ".";
    cout << "\nIf the component key is C, the component value is "
             << m['C'] << ".";
    
    cout << "\n\nEnter a key to see the correspondent maped value: ";
    cin >> whichKey;
    
    cout << "Value of your key is: " << m[whichKey] << endl;

    cout << "\nPress Enter to continue ... ";  cin.ignore(80, '\n');
     }
