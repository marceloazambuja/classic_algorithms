//
//  main.cpp
//  BinarySearch
// * this algorithm only works if the array is sorted (you should sort it first if not sorted)
//
//  Created by Marcelo Cunha de Azambuja on 6/1/19, using https://www.geeksforgeeks.org/binary-search/ as base idea.
//  Copyright © 2019 Marcelo Cunha de Azambuja. All rights reserved.
//

#include <iostream>

using namespace std;

int binarySearch (int arr[], int leftPosition, int rightPosition, int target){
    int middle;
    
    // each recursion will move these values until one pass by the other. When this happens means that the target doesn't exist in array
    if (rightPosition>=leftPosition){ //to control when a target isn't in array
        
        //find the middle position of current array:
        middle=leftPosition+ ((rightPosition-leftPosition)/2);
     
        if (arr[middle]==target)
            return (middle);
        else
            if (arr[middle]>target)
                return binarySearch(arr, leftPosition, middle-1, target);
            else
                return binarySearch(arr, middle+1, rightPosition, target);
    }
    
    //if target not found we reach here:
    return(-1);
}


int main(){
    int values[]={4, 8, 10, 12, 15, 18, 20, 22};
    int size, position, search;
    
    //ir order to discover the number of the last index of array
    size = sizeof(values)/sizeof(values[0]);
    
    cout << "Value to search: ";
    cin >> search;
    
    position = binarySearch(values, 0, size-1, search);

    if (position == -1) cout << "Value not found in the array" << endl;
    else cout << "Value found at position: " << position << endl;
    
    return(0);
}
