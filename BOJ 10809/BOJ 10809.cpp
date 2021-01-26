
#include<iostream>
using namespace std;

int main() {
    string str;
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    cin >> str;

    for (int i = 0; i < alphabet.length(); i++)
    {
        if (str.find(alphabet[i]) == string::npos)
            cout << -1 << " ";
        else {
            cout << str.find(alphabet[i]) << " ";
            continue;
        }
    }
}