#include <bits/stdc++.h>

using namespace std;

int main() {
    
    string input;
    cout << "Ready\n";
    getline(cin, input);
    
    while(input != "  "){
        if(input == "qp" || input == "pq" || input == "db" || input == "bd"){
                cout << "Mirrored pair\n";
        }
        else{
            cout << "Ordinary pair\n";
        }
        getline(cin, input);
    }

    return 0;
}