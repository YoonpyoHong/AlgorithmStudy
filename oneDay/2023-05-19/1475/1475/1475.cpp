#include <iostream>
using namespace std;

int number[10];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int N, num;	
	cin >> N;
	while (N != 0) {
		num = N % 10;
		N = N / 10;
		number[num] += 1;
	}
	int result = 0;
	int sixNine = 0;
	for (int i = 0; i < 10; i++) {
		if (i == 6 || i == 9) {
			sixNine += number[i];
		}
		else {
			result=max(result,number[i]);
		}
	}
	result = max(result, (sixNine + 1) / 2);

	cout << result;
}