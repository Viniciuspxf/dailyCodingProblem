#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> list) {
    unordered_set<int> numberSet;
    int max = list[0], result = 0;
    
    for (int i = 0; i < list.size(); i++) {
        if (list[i] > max)
            max = list[i];
            
        numberSet.insert(list[i]);
    }
    
    for (int i = 1; i <= max + 1; i++) {
        if (numberSet.find(i) == numberSet.end())
            return i;
    }
    
    return result;
}

 
int main() {
    int input;
    vector<int> list;
    int result;
    
    while (cin >> input)
        list.push_back(input);
        
    result = solution(list);

    cout << result << "\n";

    return 0;
}


