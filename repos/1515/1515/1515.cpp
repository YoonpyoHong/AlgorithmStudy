#include <iostream>
#include <string>

using namespace std;

string num;
void search();

int main() {
	cin >> num;

	search();
}


void search(){
	int idx=0;
	for (int i = 1; i < 30000; i++) {
		string testNum = to_string(i);
		for (int j = 0; j < testNum.length(); j++) {
			if (testNum[j] == num[idx]) {
				idx++;
			}
			if (idx == num.length()) {
				cout << testNum;
				return;
			}
		}
	}
}

