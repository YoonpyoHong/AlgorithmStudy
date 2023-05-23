#include <iostream>
#include <set>

using namespace std;


int N;
int city[10000];
int target;

int bsearch() {
	int start = 0;
	int end = 1000000;

	while (end - start > 1) {
		int mid = (start + end) / 2;
		int comparison = 0;
		for (int i = 0; i < N; i++) {
			if (city[i] < mid) {
				comparison += city[i];
			}
			else {
				comparison += mid;
			}
		}
		if (comparison > target) {
			end = mid;
		}
		else {
			start = mid;
		}
	}
	return start;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> city[i];
	}
	cin >> target;
	int costSum = 0;
	set<int> sorting;
	for (int i = 0; i < N; i++) {
		costSum += city[i];
		sorting.insert(city[i]);
	}
	if (costSum <= target)cout << *(--sorting.end());
	else cout << bsearch();

	return 0;
}