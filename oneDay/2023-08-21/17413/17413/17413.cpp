#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string sentence;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    getline(cin, sentence);
    string result;
    string tmp;
    int idx = 0;

    bool insideTag = false;

    while (sentence[idx] != '\0') {
        if (sentence[idx] == '<') {
            insideTag = true;
            reverse(tmp.begin(), tmp.end());
            result += tmp;
            tmp.clear();
            result.push_back(sentence[idx]);
        }
        else if (sentence[idx] == '>') {
            insideTag = false;
            result += tmp;
            tmp.clear();
            result.push_back(sentence[idx]);
        }
        else if (sentence[idx] == ' ') {
            if (!insideTag) {
                reverse(tmp.begin(), tmp.end());
            }
            result += tmp + ' ';
            tmp.clear();
        }
        else {
            tmp.push_back(sentence[idx]);
        }
        idx++;
    }

    if (!tmp.empty()) {
        reverse(tmp.begin(), tmp.end());
        result += tmp;
    }

    cout << result;
    return 0;
}
