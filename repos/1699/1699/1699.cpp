#include <iostream>

using namespace std;

int N;
int num[1000001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	int tmp;
	num[0] = 0;
	for (int i = 1; i <= N; i++) {
		tmp = 10000000;
		for (int j = 1; j * j <= i; j++) {
			if (tmp > num[i - j * j]) {
				tmp = num[i - j * j]+1;
			}
		}
		num[i] = tmp;
	}
	cout << num[N];
}