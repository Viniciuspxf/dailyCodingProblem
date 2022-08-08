#include <bits/stdc++.h>
using namespace std;


int solution(vector<int> message) {
    vector<int> counters;
    int currentCounter;
    counters.push_back(1);

    for (int i = 1; i < message.size(); i++) {

        if (i - 1 >= 0 && message[i-1] < 3 && message[i] < 7) {
            currentCounter = i-2 >= 0 ?  counters[i-1] + counters[i-2]: 2;
            counters.push_back(currentCounter);
        }
    }

    return counters[counters.size() - 1];
}



int main() {
    vector<int> message;
    int input;

    while (cin >> input)
        message.push_back(input);

    cout << solution(message) << "\n";
}