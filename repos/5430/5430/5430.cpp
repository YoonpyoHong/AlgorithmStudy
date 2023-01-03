#include <iostream>
#include <string>
#include <deque>

using namespace std;

int T, N;
string p ,order;
deque<int> numArray;

void changeToNum();
void inputData();

void doOrder();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	inputData();

}

void inputData() {
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> p >> N >> order;
		changeToNum();
		doOrder();
		
	}
}

void changeToNum() {
	char tmp = order[0];
	int tmpNum = 0;
	int cnt =1;
	while (true) {
		
		if (order[cnt] != ',' && order[cnt] !=']') {
			tmpNum = tmpNum * 10 + (order[cnt]-'0');
		}
		else {
			if (tmpNum > 0) {
				numArray.push_back(tmpNum);
				tmpNum = 0;
			}
			if (order[cnt] == ']') {
				return;
			}
		}
		cnt++;
	}
}

void doOrder() {
	bool reverse = false;
	for (int i = 0; i < p.size(); i++) {
		if (p[i] == 'R') {
			reverse = !reverse;
		}
		else if (p[i] == 'D') {
			if (numArray.empty()) {
				cout << "error\n";
				return;
			}

			if (reverse) {
				numArray.pop_back();
			}
			else {
				numArray.pop_front();
			}
		}
	}


	cout << "[";
	while(!numArray.empty()){
	if (reverse) {
		if (numArray.size() == 1) {
			cout << numArray.back();
			numArray.pop_back();
		}
		else {
			cout << numArray.back() << ',';
			numArray.pop_back();
		}
	}
	else {
		if (numArray.size() == 1) {
			cout << numArray.front();
			numArray.pop_front();
		}
		else {
			cout << numArray.front() << ',';
			numArray.pop_front();
		}
	}


	}

	cout << "]\n";
}

