#include <bits/stdc++.h>
using namespace std;

template <typename T>
class Node {
    public: 
        T value;
        Node *previousNext;

        Node(T value, Node *previousNext) {
            this->value = value;
            this->previousNext;
        }
};

template <typename T>
class linkedList {
    Node<T> *firstNode;

    Node<T> * xorOperator(Node<T> *firstArgument, Node<T> *secondArgument) {
        return (Node<T> *)( ((long long ) firstArgument ) ^ ((long long ) secondArgument));
    }

    public: 
    
        Node<T> *get(int index) {
            Node<T> * previousNode = nullptr;
            Node<T> * currentNode = firstNode;
            Node<T> * nextNode;

            for (int i = 0; i < index; i++) {
                if (currentNode == nullptr)
                    return currentNode;

                nextNode = xorOperator(previousNode, currentNode->previousNext);
                previousNode = currentNode;
                currentNode = nextNode;
            }

            return currentNode;
        }

        void insert(T element) {
            Node<T> * newNode = new Node<T>(element, nullptr);

            if (firstNode == nullptr) {
                firstNode = newNode;
                return;
            }

            Node<T> * previousNode = nullptr;
            Node<T> * currentNode = firstNode;
            Node<T> * antiPreviousNode;
            Node<T> * nextNode;

            while (currentNode != nullptr) {
                nextNode = xorOperator(previousNode, currentNode->previousNext);
                antiPreviousNode = previousNode;
                previousNode = currentNode;
                currentNode = nextNode;
            }
            newNode->previousNext = xorOperator(previousNode, nullptr);

            previousNode->previousNext = xorOperator(antiPreviousNode, newNode);
            
        }
};

int main() {
    linkedList<int> * list = new linkedList<int>;
    for (int i = 0; i < 10; i++) {
        list->insert(2*i + 5);
    }

    for (int i = 0; i < 10; i++) {
        cout << list->get(i)->value << "\n" ;
    }
    return 0;
}