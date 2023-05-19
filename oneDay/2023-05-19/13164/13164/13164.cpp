#include <iostream>
#include <algorithm>

using namespace std;

int N, K;
int students[300000];
int diff[300000];

bool compare(int a, int b) {
	return a > b;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> students[i];
	}
	int result = students[N - 1] - students[0];
	for (int i = 1; i < N; i++) {
		diff[i] = students[i] - students[i - 1];
	}
	sort(diff, diff+N, compare);
	for (int i = 0; i < K - 1; i++) {
		result -= diff[i];
	}
	cout << result;
}