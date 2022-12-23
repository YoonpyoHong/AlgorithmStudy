#include <iostream>

using namespace std;

long long num[91];
int n;

int main() {
	num[0] = 0;
	num[1] = 1;

	cin >> n;
	for (int i = 2; i <= n; i++) {
		num[i] = num[i - 1] + num[i - 2];
	}
	cout << num[n];
	
}