#include <iostream>
#include <set>
using namespace std;

int L, C;
bool checker;
char alpha[15];
int index[15];
set<char> sorting;

void makeCode(int startIdx , int len);

bool checkAvailable();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	char tmp;

	cin >> L >> C;
	for (int i = 0; i < C; i++) {
		cin >> tmp;
		sorting.insert(tmp);
	}
	int cnt = 0;
	for (auto itr = sorting.begin(); itr != sorting.end(); itr++) {
		alpha[cnt] = *itr;
		cnt++;
	}

	makeCode(0 , -1);
}

void makeCode(int startIdx , int len) {
	
	if (len == L-1) {
		if (checkAvailable()) {
			for (int j = 0; j < L; j++) {
				cout << alpha[index[j]];
			}
			cout << "\n";
		}
	}
	else {
		len++;
		for (int i = startIdx; i < C; i++) {
			
			index[len] = i;
			makeCode(i + 1, len);
		}

	}
}

bool checkAvailable() {
	bool availableV = false;
	int availableC = 0;
	for (int j = 0; j < L; j++) {
		if (alpha[index[j]] == 'a' || alpha[index[j]] == 'e' || alpha[index[j]] == 'i' || alpha[index[j]] == 'o' || alpha[index[j]] == 'u') {
			availableV = true;
		}
		else {
			availableC++;
		}
	}
	if (availableV && availableC >= 2) {
		return true;
	}
	else {
		return false;
	}
}
