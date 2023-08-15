#include <iostream>

using namespace std;
int disk[100000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int N, M;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> disk[i];
	}
	int start = 0;
	int end = 1000000001;
	int mid;
	while (start + 1 < end) {
		mid = (start + end) / 2;
		int idx = 1;
		int length = 0;
		for (int i = 0; i < N; i++) {
			if (disk[i] > mid) {
				idx = M + 1;
				break;
			}
			if (length + disk[i] <= mid) {
				length += disk[i];
			}
			else {
				length = disk[i];
				idx += 1;
			}
		}
		if (idx > M) {
			start = mid;
		}
		else {
			end = mid;
		}
	}
	cout << end;
}