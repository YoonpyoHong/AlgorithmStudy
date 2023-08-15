#include <iostream>
#include <vector>
#include <string>

using namespace std;

string sentence;
string bomb;
int bombLength;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> sentence;
	cin >> bomb;
	bombLength = bomb.size();
	vector<char> resultSentence;

	for (int i = 0; i < sentence.size(); i++) {
		resultSentence.push_back(sentence[i]);
		if (sentence[i] == bomb[bomb.size()-1]) {
			int currLength =resultSentence.size();
			if (currLength >= bombLength) {
				for (int j = 0; j < bombLength; j++) {
					if (resultSentence[currLength - bombLength + j] != bomb[j]) {
						break;
					}
					if (j == bombLength - 1) {
						for (int j = 0; j < bombLength; j++) resultSentence.pop_back();
					}
				}
			}
		}
	}

	if (resultSentence.empty()) {
		cout << "FRULA";
	}
	else {
		for (int i = 0; i < resultSentence.size(); i++) {
			cout << resultSentence.at(i);
		}
	}
}
