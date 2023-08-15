#include <iostream>
#include <algorithm>

using namespace std;

int N, L;
int hole[1000];
int cnt = 1;

void input() {
	cin >> N >> L;
	for (int i = 0; i < N; i++) {
		cin >> hole[i];
	}
	sort(hole, hole+N);
}

void taping() {
	int idx = 1;
	int pos = hole[0];
	while(idx < N){
		if (hole[idx] > pos + L - 1) {
			pos = hole[idx];
			cnt++;
		}
		idx++;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	input();
	taping();
	cout << cnt;
}