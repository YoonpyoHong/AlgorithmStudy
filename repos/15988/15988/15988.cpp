#include <iostream>

using namespace std;

void inputData();
void search();
int T, n;
long searchArr[1000001];

int main() {
	inputData();
}

void inputData() {
	cin >> T;
	searchArr[0] = 1;
	searchArr[1] = 1;
	searchArr[2] = 2;
	

	
	
	for (int i = 0; i < T; i++) {
		cin >> n;
		search();
		cout << searchArr[n] << '\n';
	}
}

void search() {
	for (int i = 3; i <= n; i++) {
		searchArr[i] = (searchArr[i - 1] + searchArr[i - 2] + searchArr[i - 3])% 1000000009;
	}
}