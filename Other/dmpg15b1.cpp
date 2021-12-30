#include <bits/stdc++.h>

using namespace std;

int main() {
        string phoneNumber;
    int iters;
    cin >> iters;
    cin.ignore();
    for(int i = 0; i < iters; i++){
        getline(cin, phoneNumber);
        if(phoneNumber.length() == 10 && (phoneNumber.substr(0, 3) == "416" || phoneNumber.substr(0, 3) == "647")){
            cout << "(" << phoneNumber.substr(0, 3) << ")-" << phoneNumber.substr(3, 3) << "-" << phoneNumber.substr(6, 4) << endl;
        }
        else{
            cout << "not a phone number\n";
        }
    }
    return 0;
}