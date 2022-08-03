#include <bits/stdc++.h>
using namespace std;

vector<int> solutionWithoutDivision(vector<int> list) {
    vector<int> result(list.size()), auxiliarOne(list.size()), auxiliarTwo(list.size());
    
    auxiliarOne[0] = list[0];
    auxiliarTwo[list.size() - 1] =list[list.size() - 1];
    
    for (int i = 1; i < list.size(); i++)
        auxiliarOne[i] = list[i]*auxiliarOne[i-1];
    
    for (int i = list.size() - 2; i >= 0; i--)
        auxiliarTwo[i] = list[i]*auxiliarTwo[i+1];
    
    result[0] = auxiliarTwo[1];
    result[list.size() - 1]  = auxiliarOne[list.size() - 2];
    
    
    for (int i = 1; i < list.size() - 1; i++)
        result[i] =  auxiliarOne[i - 1]*auxiliarTwo[i + 1];

    return result;
}

vector<int> solution(vector<int> list) {
    vector<int> result;
    int accumulated = 1;
    
    for (int i = 0; i < list.size(); i++)
        accumulated *= list[i];
    
    for (int i = 0; i < list.size(); i++)
        result.push_back(accumulated/list[i]);
    
    return result;
}
 
int main() {
    int input;
    vector<int> list, result;
    
    while (cin >> input)
        list.push_back(input);
        
    result = solutionWithoutDivision(list);

    for (int i = 0; i < result.size(); i++)
        cout << result[i] << " ";
    cout << "\n";
    return 0;
}

