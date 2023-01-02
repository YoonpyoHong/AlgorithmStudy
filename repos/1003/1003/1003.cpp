#include <iostream>

using namespace std;
int T, N;
pair<int, int> fibo[41];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	fibo[0].first = 1;
	fibo[1].second = 1;
	fibo[2].first = 1;
	fibo[2].second = 1;
	for (int i = 3; i <= 40; i++) {
		fibo[i] = { fibo[i - 2].first + fibo[i - 1].first,fibo[i - 2].second + fibo[i - 1].second };
	}
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		
		cout << fibo[N].first << " " << fibo[N].second<< "\n";
	}
}

