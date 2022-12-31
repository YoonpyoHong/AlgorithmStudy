#include <iostream>
#include <set>

using namespace std;

int N;
int X[1000000];
int Xprime[1000000];
set<int> Xset;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> X[i];
		Xset.insert(X[i]);
	}
	int cnt = 0;
	for (auto itr = Xset.begin(); itr != Xset.end(); itr++) {
		for (int i = 0; i < N; i++) {
			if (X[i] == *itr) {
				Xprime[i] = cnt;
			}
		}
		cnt++;
	}
	for (int i = 0; i < N; i++) {
		cout << Xprime[i] << " ";
	}
	
}