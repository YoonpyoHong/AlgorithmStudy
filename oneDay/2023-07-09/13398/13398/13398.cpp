#include <iostream>

using namespace std;

int DP[1000001][2];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	int newNum;
	cin >> newNum;
	DP[0][0] = newNum;
	DP[0][1] = 0;
	for (int i = 1; i < T; i++) {
		cin >> newNum;
		DP[i][0] = DP[i - 1][0] + newNum;
		DP[i][1] = max(DP[i-1][1] + newNum, DP[i-1][0]);
	}
	cout << max(DP[T - 1][0], DP[T - 1][1]);
}