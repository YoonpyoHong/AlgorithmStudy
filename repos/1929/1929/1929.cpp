#include <iostream>

using namespace std;

int M, N;

bool check[1000001];

int main() {
	cin >> M >> N;
	for (int i = 2; i <= N; i++) {
		if (check[i] == false) {
			if (i >= M) {
				cout << i << "\n";
			}
			for (int j = i; j <= N; j += i) {
				check[j] = true;
			}
		}
	}
}

