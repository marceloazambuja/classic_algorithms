//
//  main.cpp
//  BinarySearchTree
//  Find the minimum value in Binary Search Tree (BST)
//
// Considering that in BST each value from left to each root is always less than the root value, to find the very minimum value it's needed to read each left node until reach the NULL value, i.e., the most left node is always the minimum value in BST.

//  Created by Marcelo Cunha de Azambuja on 6/3/19, based on https://www.geeksforgeeks.org/find-the-minimum-element-in-a-binary-search-tree/
//

#include <iostream>

using namespace std;

struct node {
    int value;
    node *left;
    node *right;
};

struct node* newNode (int newValue){
    struct node* node = (struct node*) malloc(sizeof(struct node));
    node->value=newValue;
    node->left=NULL;
    node->right=NULL;
    
    return (node);
}

struct node* insertNode (struct node* position, int newData){
    if (position==NULL)
        return(newNode(newData));
    else{
        if (newData < position->value)
            position->left=insertNode(position->left, newData);
        else
            position->right=insertNode(position->right, newData);
        
        //if nothing works return the start position
        return(position);
    }
}

int minValue (struct node* firstNode){
    struct node* current = firstNode;
    
    while (current->left!=NULL){
        current = current->left;
    }
    return (current->value);
}

int main(){
    struct node* root = NULL;
    root=insertNode(root, 90);
    insertNode(root, 30);
    insertNode(root, 80);
    insertNode(root, 35);
    insertNode(root, 20);
    insertNode(root, 70);
    
    
    cout << "Minimum value of Binary Tree: " << minValue(root) << "\n";
    
    return(0);
}
