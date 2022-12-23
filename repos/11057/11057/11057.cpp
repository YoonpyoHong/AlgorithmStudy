#include <iostream>

using namespace std;

int  num[1000][10];
int n;

int main() {
	for (int i = 0; i < 10; i++) {
		num[1][i] = 1;
	}
	cin >> n;

	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			int sum = 0;
			for (int k = 0; k <= j; k++) {
				sum += (num[i - 1][k]%10007);
			}
			
			num[i][j] = sum%10007;
		}
	}

	int sum = 0;
	for (int i = 0; i < 10; i++) {
		sum += (num[n][i]%10007);
	}
	cout << sum % 10007;
		
}