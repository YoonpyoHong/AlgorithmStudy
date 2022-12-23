#include <iostream>

using namespace std;

void inputData();
void search();
int T;
int n;
int numArray[12];

int main(){
	

	
	numArray[0] = 1;
	numArray[1] = 1;
	numArray[2] = 2;
	inputData();
	
	
}

void inputData() {
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n;
		search();
		cout << numArray[n] <<"\n";
	}
}

void search() {
	for (int i = 3; i <= n; i++) {
		numArray[i] = numArray[i - 3] + numArray[i - 2] + numArray[i - 1];
	}
}

