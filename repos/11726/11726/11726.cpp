#include <iostream>

using namespace std;

int prob[1001];
int n;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	prob[0] = 1;
	prob[1] = 1;
	for (int i = 2; i <= n; i++) {
		prob[i] = (prob[i - 2] + prob[i - 1]) % 10007;
	}
	cout << prob[n];
}