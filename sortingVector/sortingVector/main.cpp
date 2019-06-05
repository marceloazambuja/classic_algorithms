//
//  main.cpp
//  sortingVector
//
//  Created by Marcelo Cunha de Azambuja on 6/5/19.
//  Copyright © 2019 Marcelo Cunha de Azambuja. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> myVector{30, 12, 90, 4, 3, 33, 32, 2};
    
    sort(myVector.begin(), myVector.end());
    
    cout << "Sorted vector: " << endl;
    for (auto x : myVector)
        cout << x << " | ";
    
    cout << endl;
    
    return 0;
}
