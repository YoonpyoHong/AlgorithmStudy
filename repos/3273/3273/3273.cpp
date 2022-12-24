#include <iostream>
#include <set>

using namespace std;
int N, X, tmp, c;
set<int> s;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> tmp;
		s.insert(tmp);
	}
	cin >> X;

	for (auto itr = s.begin(); itr != s.end(); itr++) {
		if (s.find(X - *itr) != s.end()) {
			c++;
		}
	}
	cout << c / 2;
}