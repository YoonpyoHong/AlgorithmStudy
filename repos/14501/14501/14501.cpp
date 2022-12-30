#include <iostream>

using namespace std;

int N;
pair<int, int> schdule[16];
int maxIncome[17];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> schdule[i].first;
		cin >> schdule[i].second;
	}

	for (int i = 1; i <= N; i++) {
		maxIncome[i] = max(maxIncome[i], maxIncome[i - 1]);
		if(i+schdule[i].first<=N+1){
			maxIncome[i + schdule[i].first] = max(maxIncome[i + schdule[i].first], maxIncome[i] + schdule[i].second);
		}
	}

	cout << max(maxIncome[N+1], maxIncome[N]);
}

