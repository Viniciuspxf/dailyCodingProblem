/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <bits/stdc++.h>
using namespace std;

class UnivalInfo {
    public:
        bool isUnival;
        int univalChildrenCounter;
        int childValue;
        
        UnivalInfo(bool isUnival, int univalChildrenCounter, int childValue) {
            this->isUnival = isUnival;
            this->univalChildrenCounter = univalChildrenCounter;
            this->childValue = childValue;
        }
};

class Node {
    public:
        int value;
        Node * leftChild;
        Node * rightChild;
        
        Node(int value, Node *leftChild, Node *rightChild) {
            this->value = value;
            this->leftChild = leftChild;
            this->rightChild = rightChild;
        }
        
        
};


UnivalInfo getUnivalSubtreesInfo(Node* root) {
    UnivalInfo currentUnival(true, 0, root->value);
    
    if (root->leftChild == nullptr && root->rightChild == nullptr) {
        currentUnival.univalChildrenCounter = 1;
        return currentUnival;
    }
    
    
    if (root->leftChild != nullptr) {
        UnivalInfo leftUnivalInfo = getUnivalSubtreesInfo(root->leftChild);
        
        if (leftUnivalInfo.childValue != root->value || !leftUnivalInfo.isUnival) {
            currentUnival.isUnival = false;
        }
        
        currentUnival.univalChildrenCounter += leftUnivalInfo.univalChildrenCounter;
        
    }
    
    if (root->rightChild != nullptr) {
        UnivalInfo rightUnivalInfo = getUnivalSubtreesInfo(root->rightChild);
        
        if (rightUnivalInfo.childValue != root->value || !rightUnivalInfo.isUnival) {
            currentUnival.isUnival = false;
        }
        
        currentUnival.univalChildrenCounter += rightUnivalInfo.univalChildrenCounter;
    }
    
    currentUnival.univalChildrenCounter += currentUnival.isUnival;

    return currentUnival;
}

int main() {
    Node * root
    = new Node(0, 
    new Node(1, nullptr, nullptr), 
    new Node(0, 
    new Node(1, 
    new Node(1, nullptr, nullptr), 
    new Node(1, nullptr, nullptr)), 
    new Node(0, nullptr, nullptr)));
    cout<< getUnivalSubtreesInfo(root).univalChildrenCounter << "\n";

    return 0;
}
