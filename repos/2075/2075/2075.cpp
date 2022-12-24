#include <iostream>
#include <queue>

using namespace std;

int N;
priority_queue<int> num;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int numnum;
	cin >> N;

	for (int i = 0; i < N; i++) {
			cin >> numnum;
			num.push(-numnum);
	}
	for (int i = N; i < N*N; i++) {
		cin >> numnum;
		num.push(-numnum);
		num.pop();
	}
	cout << -1 * num.top();
}
